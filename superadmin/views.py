from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db.models import Q
from restaurants.models import Restaurant, MenuItem
from accounts.models import User
from .decorators import superadmin_required


@superadmin_required
def dashboard(request):
    """Super admin dashboard with platform statistics"""
    total_restaurants = Restaurant.objects.count()
    active_restaurants = Restaurant.objects.filter(is_active=True).count()
    inactive_restaurants = total_restaurants - active_restaurants
    total_items = MenuItem.objects.count()
    total_users = User.objects.filter(role=User.ROLE_RESTAURANT_ADMIN).count()
    
    # Recent restaurants
    recent_restaurants = Restaurant.objects.select_related('owner').order_by('-created_at')[:8]
    
    context = {
        'total_restaurants': total_restaurants,
        'active_restaurants': active_restaurants,
        'inactive_restaurants': inactive_restaurants,
        'total_items': total_items,
        'total_users': total_users,
        'recent_restaurants': recent_restaurants,
    }
    
    return render(request, 'superadmin/dashboard.html', context)


@superadmin_required
def restaurants_list(request):
    """List all restaurants with search"""
    query = request.GET.get('q', '')
    
    restaurants = Restaurant.objects.select_related('owner').all()
    
    if query:
        restaurants = restaurants.filter(
            Q(name__icontains=query) | Q(owner__email__icontains=query)
        )
    
    return render(request, 'superadmin/restaurants.html', {
        'restaurants': restaurants,
        'query': query
    })


@superadmin_required
@require_POST
def toggle_restaurant(request, pk):
    """Toggle restaurant active status"""
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.is_active = not restaurant.is_active
    restaurant.save()
    
    status = 'activated' if restaurant.is_active else 'deactivated'
    messages.success(request, f'Restaurant "{restaurant.name}" {status}.')
    
    return redirect('superadmin:restaurants')


@superadmin_required
@require_POST
def delete_restaurant(request, pk):
    """Permanently delete a restaurant and all its data"""
    restaurant = get_object_or_404(Restaurant, pk=pk)
    name = restaurant.name
    owner = restaurant.owner
    
    # Delete restaurant (cascade will delete categories, items)
    restaurant.delete()
    
    # Delete owner user account
    owner.delete()
    
    messages.success(request, f'Restaurant "{name}" and all its data permanently deleted.')
    
    return redirect('superadmin:restaurants')
