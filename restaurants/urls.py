from django.urls import path
from . import views

app_name = 'restaurants'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:pk>/edit/', views.edit_category, name='edit_category'),
    path('categories/<int:pk>/delete/', views.delete_category, name='delete_category'),
    path('items/', views.menu_items, name='menu_items'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('items/<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('items/<int:pk>/toggle/', views.toggle_availability, name='toggle_availability'),
    path('qr-code/', views.qr_code_view, name='qr_code_view'),
]
