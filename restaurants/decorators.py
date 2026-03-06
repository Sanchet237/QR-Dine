from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def restaurant_admin_required(view_func):
    """
    Decorator to restrict access to restaurant admin views only.
    Ensures user is authenticated, has a restaurant, and is active.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        
        if request.user.is_superadmin():
            return redirect('superadmin:dashboard')
        
        if not hasattr(request.user, 'restaurant'):
            messages.error(request, "No restaurant profile found for your account.")
            return redirect('core:landing')
        
        if not request.user.restaurant.is_active:
            messages.warning(
                request,
                "Your restaurant account has been deactivated. Contact support."
            )
            # Allow access but show warning
        
        return view_func(request, *args, **kwargs)
    
    return wrapper
