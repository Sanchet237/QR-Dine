from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from django_ratelimit.decorators import ratelimit
from .forms import RegisterForm, LoginForm


@ratelimit(key='ip', rate='10/m', block=True)
def register_view(request):
    """Restaurant registration view"""
    if request.user.is_authenticated:
        if request.user.is_superadmin():
            return redirect('superadmin:dashboard')
        return redirect('restaurants:dashboard')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to QRDine! Your restaurant has been registered.")
            return redirect('restaurants:dashboard')
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})


@ratelimit(key='ip', rate='10/m', block=True)
def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        if request.user.is_superadmin():
            return redirect('superadmin:dashboard')
        return redirect('restaurants:dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Redirect based on role
            if user.is_superadmin():
                return redirect('superadmin:dashboard')
            else:
                return redirect('restaurants:dashboard')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


@require_POST
def logout_view(request):
    """User logout view — POST only to prevent CSRF logout attacks"""
    logout(request)
    messages.info(request, "You've been logged out successfully.")
    return redirect('core:landing')
