from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from . import views
from restaurants.models import Restaurant


class MenuSitemap(Sitemap):
    """Sitemap for all active restaurant public menus"""
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Restaurant.objects.filter(is_active=True)

    def location(self, obj):
        return obj.get_menu_url()


sitemaps = {'menus': MenuSitemap}

app_name = 'core'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
