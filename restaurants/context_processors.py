def restaurant_context(request):
    """
    Makes `restaurant` available in all templates for authenticated restaurant admins.
    Avoids repeated `request.user.restaurant` calls in templates.
    """
    ctx = {'restaurant': None}
    if request.user.is_authenticated and hasattr(request.user, 'restaurant'):
        ctx['restaurant'] = request.user.restaurant
    return ctx
