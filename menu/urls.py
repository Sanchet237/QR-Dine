from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('<slug:slug>/', views.menu_viewer, name='viewer'),
]
