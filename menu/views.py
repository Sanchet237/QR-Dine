from django.shortcuts import render, get_object_or_404
from django.http import Http404
from restaurants.models import Restaurant


def menu_viewer(request, slug):
    """
    Public menu viewer - accessible via QR code scan.
    No authentication required.
    """
    try:
        restaurant = Restaurant.objects.prefetch_related(
            'categories__items'
        ).get(slug=slug)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant not found")
    
    # If restaurant is inactive, show unavailable page
    if not restaurant.is_active:
        return render(request, 'menu/unavailable.html', {
            'restaurant': restaurant
        }, status=200)
    
    # Get categories with their items
    categories = restaurant.categories.prefetch_related('items').all()
    
    # Get all items for search/filtering
    all_items = restaurant.menu_items.select_related('category').all()
    
    return render(request, 'menu/viewer.html', {
        'restaurant': restaurant,
        'categories': categories,
        'all_items': all_items
    })
