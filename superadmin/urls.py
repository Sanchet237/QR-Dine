from django.urls import path
from . import views

app_name = 'superadmin'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('restaurants/', views.restaurants_list, name='restaurants'),
    path('restaurants/<int:pk>/toggle/', views.toggle_restaurant, name='toggle_restaurant'),
    path('restaurants/<int:pk>/delete/', views.delete_restaurant, name='delete_restaurant'),
]
