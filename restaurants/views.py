from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Restaurant, Category, MenuItem
from .forms import RestaurantProfileForm, CategoryForm, MenuItemForm
from .decorators import restaurant_admin_required
from .utils import generate_qr_code


@restaurant_admin_required
def dashboard(request):
    """Restaurant dashboard overview"""
    restaurant = request.user.restaurant
    
    context = {
        'total_items': restaurant.total_items,
        'available_items': restaurant.available_items_count,
        'sold_out_items': restaurant.sold_out_count,
        'total_categories': restaurant.categories.count(),
        'recent_items': restaurant.menu_items.select_related('category')[:8],
    }
    
    return render(request, 'restaurants/dashboard.html', context)


@restaurant_admin_required
def profile(request):
    """Edit restaurant profile"""
    restaurant = request.user.restaurant
    
    if request.method == 'POST':
        form = RestaurantProfileForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('restaurants:profile')
    else:
        form = RestaurantProfileForm(instance=restaurant)
    
    return render(request, 'restaurants/profile.html', {
        'form': form,
        'restaurant': restaurant
    })


@restaurant_admin_required
def categories(request):
    """List and add categories"""
    restaurant = request.user.restaurant
    editing = None
    
    # Check if editing a category
    edit_id = request.GET.get('edit')
    if edit_id:
        editing = get_object_or_404(Category, pk=edit_id, restaurant=restaurant)
    
    if request.method == 'POST':
        if editing:
            form = CategoryForm(request.POST, instance=editing)
        else:
            form = CategoryForm(request.POST)
        
        if form.is_valid():
            category = form.save(commit=False)
            category.restaurant = restaurant
            category.save()
            
            if editing:
                messages.success(request, f'Category "{category.name}" updated.')
            else:
                messages.success(request, f'Category "{category.name}" added.')
            
            return redirect('restaurants:categories')
    else:
        form = CategoryForm(instance=editing) if editing else CategoryForm()
    
    categories_list = restaurant.categories.prefetch_related('items').all()
    
    return render(request, 'restaurants/categories.html', {
        'categories': categories_list,
        'form': form,
        'editing': editing
    })


@restaurant_admin_required
def edit_category(request, pk):
    """Edit category - redirects to categories page with edit parameter"""
    category = get_object_or_404(Category, pk=pk, restaurant=request.user.restaurant)
    return redirect(f"{request.path.replace(f'/edit/','')}?edit={pk}")


@restaurant_admin_required
@require_POST
def delete_category(request, pk):
    """Delete a category"""
    category = get_object_or_404(Category, pk=pk, restaurant=request.user.restaurant)
    name = category.name
    category.delete()
    messages.success(request, f'Category "{name}" deleted. Items are now uncategorised.')
    return redirect('restaurants:categories')


@restaurant_admin_required
def menu_items(request):
    """List all menu items"""
    restaurant = request.user.restaurant
    category_filter = request.GET.get('category')
    
    items = restaurant.menu_items.select_related('category')
    
    if category_filter:
        items = items.filter(category_id=category_filter)
    
    categories_list = restaurant.categories.all()
    
    return render(request, 'restaurants/menu_items.html', {
        'items': items,
        'categories': categories_list,
        'selected_category': int(category_filter) if category_filter else None
    })


@restaurant_admin_required
def add_item(request):
    """Add a new menu item"""
    restaurant = request.user.restaurant
    
    if request.method == 'POST':
        form = MenuItemForm(restaurant, request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.restaurant = restaurant
            item.save()
            messages.success(request, f'"{item.name}" added to your menu.')
            return redirect('restaurants:menu_items')
    else:
        form = MenuItemForm(restaurant)
    
    return render(request, 'restaurants/add_item.html', {'form': form})


@restaurant_admin_required
def edit_item(request, pk):
    """Edit a menu item"""
    restaurant = request.user.restaurant
    item = get_object_or_404(MenuItem, pk=pk, restaurant=restaurant)
    
    if request.method == 'POST':
        form = MenuItemForm(restaurant, request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{item.name}" updated.')
            return redirect('restaurants:menu_items')
    else:
        form = MenuItemForm(restaurant, instance=item)
    
    return render(request, 'restaurants/edit_item.html', {
        'form': form,
        'item': item
    })


@restaurant_admin_required
@require_POST
def delete_item(request, pk):
    """Delete a menu item"""
    item = get_object_or_404(MenuItem, pk=pk, restaurant=request.user.restaurant)
    name = item.name
    item.delete()
    messages.success(request, f'"{name}" deleted from your menu.')
    return redirect('restaurants:menu_items')


@restaurant_admin_required
@require_POST
def toggle_availability(request, pk):
    """Toggle item availability (AJAX endpoint)"""
    try:
        item = get_object_or_404(MenuItem, pk=pk, restaurant=request.user.restaurant)
        item.is_available = not item.is_available
        item.save()
        
        return JsonResponse({
            'status': 'ok',
            'is_available': item.is_available,
            'item_id': item.pk,
            'label': 'Available' if item.is_available else 'Sold Out'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)


@restaurant_admin_required
def qr_code_view(request):
    """Generate and display QR code"""
    restaurant = request.user.restaurant
    
    # Generate QR code
    qr_path = generate_qr_code(restaurant, request)
    
    menu_url = request.build_absolute_uri(restaurant.get_menu_url())
    
    return render(request, 'restaurants/qr_code.html', {
        'qr_path': qr_path,
        'menu_url': menu_url,
        'restaurant': restaurant
    })
