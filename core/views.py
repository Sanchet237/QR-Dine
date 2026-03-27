from django.shortcuts import render
from django.http import HttpResponse
from restaurants.models import Restaurant, MenuItem


def landing(request):
    """Landing page view"""
    total_restaurants = Restaurant.objects.filter(is_active=True).count()
    total_items = MenuItem.objects.count()
    
    return render(request, 'core/landing.html', {
        'total_restaurants': total_restaurants,
        'total_items': total_items,
    })


def terms(request):
    """Terms of Service page"""
    return render(request, 'core/terms.html')


def privacy(request):
    """Privacy Policy page"""
    return render(request, 'core/privacy.html')


def robots_txt(request):
    """robots.txt — disallow crawling of private/admin routes"""
    lines = [
        'User-agent: *',
        'Disallow: /admin/',
        'Disallow: /dashboard/',
        'Disallow: /accounts/',
        'Disallow: /superadmin/',
        'Allow: /',
        'Allow: /menu/',
        '',
        f'Sitemap: {request.build_absolute_uri("/sitemap.xml")}',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


def custom_404(request, exception):
    """Custom 404 handler"""
    return render(request, '404.html', status=404)


def custom_500(request):
    """Custom 500 handler"""
    return render(request, '500.html', status=500)
