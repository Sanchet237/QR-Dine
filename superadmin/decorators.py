from functools import wraps
from django.shortcuts import redirect


def superadmin_required(view_func):
    """
    Decorator to restrict access to super admin views only.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        
        if not request.user.is_superadmin():
            return redirect('restaurants:dashboard')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper
