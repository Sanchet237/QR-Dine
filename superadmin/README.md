# 🛡️ Super Admin Module

This module provides platform-level administration capabilities for managing restaurants, users, and overall system health.

---

## 📋 Overview

The superadmin module provides:
- Platform dashboard with overview stats
- Restaurant management (activate/deactivate/delete)
- User management
- System monitoring
- Bulk operations

---

## 🏗️ Architecture

### Access Control

Only users with `role='superadmin'` can access this module. Enforced via `@superadmin_required` decorator.

---

## 📁 File Structure

```
superadmin/
├── __init__.py
├── admin.py          # Django admin customizations
├── apps.py           # App configuration
├── models.py         # No custom models
├── views.py          # Superadmin views
├── decorators.py     # @superadmin_required decorator
├── tests.py          # Unit tests
├── urls.py           # URL routing
└── migrations/       # (Empty, no models)
```

---

## 🔗 URL Routes

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/superadmin/` | `superadmin_dashboard` | Platform overview dashboard |
| `/superadmin/restaurants/` | `restaurants_list` | View all restaurants |
| `/superadmin/restaurant/<id>/toggle/` | `toggle_restaurant` | Activate/deactivate restaurant |
| `/superadmin/restaurant/<id>/delete/` | `delete_restaurant` | Delete restaurant |

---

## 🎨 Key Views

### `superadmin_dashboard(request)`
- **Decorator:** `@login_required`, `@superadmin_required`
- **Template:** `superadmin/dashboard.html`
- **Logic:**
  - Display total restaurants count
  - Show active vs inactive restaurants
  - List total users
  - Quick stats on menu items across platform
  - Recent registrations

**Context:**
```python
{
    'total_restaurants': 42,
    'active_restaurants': 38,
    'inactive_restaurants': 4,
    'total_users': 45,
    'total_menu_items': 1250,
    'recent_restaurants': [...]
}
```

### `restaurants_list(request)`
- **Template:** `superadmin/restaurants.html`
- **Logic:**
  - List all restaurants with details
  - Show status (active/inactive)
  - Provide quick actions (toggle status, delete)
  - Search and filter capabilities

### `toggle_restaurant(request, restaurant_id)`
- **Method:** POST
- **Logic:**
  - Toggle `is_active` field for restaurant
  - Inactive restaurants cannot be accessed by customers
- **Redirects:** Back to restaurants list

### `delete_restaurant(request, restaurant_id)`
- **Method:** POST
- **Logic:**
  - Permanently delete restaurant and associated data
  - Cascade delete: menu items, categories, user
  - Confirmation required
- **Redirects:** Back to restaurants list

---

## 🛡️ Decorators

### `@superadmin_required` (`decorators.py`)

```python
from functools import wraps
from django.shortcuts import redirect

def superadmin_required(view_func):
    """
    Decorator to restrict access to superadmin users only
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        if request.user.role != 'superadmin':
            return redirect('dashboard')  # Redirect non-superadmins
        
        return view_func(request, *args, **kwargs)
    return wrapper
```

**Usage:**
```python
@login_required
@superadmin_required
def superadmin_dashboard(request):
    # View logic
    pass
```

---

## 📊 Dashboard Statistics

The superadmin dashboard shows:

### Restaurant Metrics
- Total restaurants registered
- Active restaurants
- Inactive/suspended restaurants
- Registration trend (this month vs last month)

### User Metrics
- Total users (restaurant admins)
- Active users (logged in last 30 days)
- New registrations this week

### Menu Metrics
- Total menu items across all restaurants
- Average items per restaurant
- Most popular categories

### System Health
- Database size
- Media storage usage
- Uptime status

---

## 🔧 Admin Operations

### Activate/Deactivate Restaurant

**Use case:** Temporarily disable a restaurant's menu without deleting it.

```python
def toggle_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    restaurant.is_active = not restaurant.is_active
    restaurant.save()
    
    messages.success(request, f'{restaurant.name} is now {"active" if restaurant.is_active else "inactive"}')
    return redirect('superadmin:restaurants_list')
```

**Effect:**
- Menu becomes inaccessible at `/menu/<slug>/`
- Restaurant admin can still login and edit
- Dashboard shows "Restaurant Inactive" warning

### Delete Restaurant

**Use case:** Permanently remove restaurant and all data.

```python
def delete_restaurant(request, restaurant_id):
    if request.method == 'POST':
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        restaurant_name = restaurant.name
        
        # Cascade delete: menu items, categories, QR codes, images
        restaurant.delete()
        
        messages.success(request, f'{restaurant_name} has been deleted')
        return redirect('superadmin:restaurants_list')
    
    # Show confirmation page for GET requests
    return render(request, 'superadmin/confirm_delete.html')
```

**Cascade behavior:**
- Deletes all menu items
- Deletes all categories
- Deletes uploaded images (logo, QR code, menu item images)
- Keeps user account (can be deleted separately if needed)

---

## 🔍 Search and Filter

### Restaurant Search

```html
<input type="text" id="restaurantSearch" placeholder="Search by name or email...">
```

```javascript
// Real-time search
document.getElementById('restaurantSearch').addEventListener('input', function(e) {
    const term = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('.restaurant-row');
    
    rows.forEach(row => {
        const name = row.dataset.name.toLowerCase();
        const email = row.dataset.email.toLowerCase();
        
        if (name.includes(term) || email.includes(term)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
});
```

### Filter Options

- **By Status:** All / Active / Inactive
- **By Registration Date:** Today / Last 7 days / Last 30 days / All time
- **By Activity:** Active (has menu items) / Empty (no menu items)

---

## 🔒 Security Considerations

### Access Control
- Only `role='superadmin'` users can access
- Double decorator protection (`@login_required` + `@superadmin_required`)
- CSRF protection on all POST requests

### Sensitive Operations
- Delete operations require confirmation
- Activity log (future enhancement)
- Audit trail for admin actions

### Data Privacy
- Superadmin cannot view user passwords (hashed)
- PII (personally identifiable information) handled securely

---

## 📈 Reporting (Future Enhancement)

### Platform Growth Report
- Registrations over time (chart)
- Menu items added over time
- Active vs inactive restaurants trend

### Restaurant Performance
- Most viewed menus
- Largest restaurants (by menu items)
- Restaurants with no activity

### User Engagement
- Login frequency
- Dashboard usage stats
- QR code scans (if tracking enabled)

---

## 🧪 Testing

Run tests:
```bash
python manage.py test superadmin
```

Test cases:
- Superadmin can access dashboard
- Restaurant admin cannot access superadmin panel
- Anonymous user redirected to login
- Toggle restaurant status works
- Delete restaurant cascades correctly

---

## 🚀 Management Commands

### Create Superadmin User

```bash
python manage.py createsuperuser
# When prompted for role, enter: superadmin
```

Or programmatically:
```python
from accounts.models import CustomUser

superuser = CustomUser.objects.create_superuser(
    username='admin',
    email='admin@qrdine.com',
    password='secure_password_here',
    role='superadmin'
)
```

---

## 📊 Dashboard UI Components

### Stats Cards

```html
<div class="stat-card">
    <h3>Total Restaurants</h3>
    <p class="stat-number">42</p>
    <span class="stat-change">+5 this month</span>
</div>
```

### Restaurants Table

```html
<table class="restaurants-table">
    <thead>
        <tr>
            <th>Restaurant Name</th>
            <th>Email</th>
            <th>Status</th>
            <th>Menu Items</th>
            <th>Registered</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for restaurant in restaurants %}
        <tr>
            <td>{{ restaurant.name }}</td>
            <td>{{ restaurant.email }}</td>
            <td>
                {% if restaurant.is_active %}
                    <span class="badge-active">Active</span>
                {% else %}
                    <span class="badge-inactive">Inactive</span>
                {% endif %}
            </td>
            <td>{{ restaurant.menuitem_set.count }}</td>
            <td>{{ restaurant.created_at|date:"M d, Y" }}</td>
            <td>
                <button onclick="toggleStatus({{ restaurant.id }})">
                    Toggle Status
                </button>
                <button onclick="deleteRestaurant({{ restaurant.id }})">
                    Delete
                </button>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

---

## 🔄 Future Enhancements

- [ ] Bulk operations (activate/deactivate multiple)
- [ ] Export data (CSV, PDF reports)
- [ ] Email notifications to restaurants
- [ ] Subscription management (if paid plans added)
- [ ] Platform settings configuration
- [ ] Advanced analytics dashboard
- [ ] User impersonation (for support)

---

## 📚 Related Modules

- **[Accounts](../accounts/README.md)** — User and role management
- **[Restaurants](../restaurants/README.md)** — Restaurant data being managed

---

## 🆘 Troubleshooting

### Issue: Cannot access superadmin panel
**Solution:** Ensure user has `role='superadmin'`. Check with:
```python
python manage.py shell
>>> from accounts.models import CustomUser
>>> user = CustomUser.objects.get(username='admin')
>>> user.role
'superadmin'  # Should be this
```

### Issue: Delete restaurant fails
**Solution:** Check for foreign key constraints. Ensure cascade delete is configured in models.

### Issue: Stats not updating
**Solution:** Clear Django cache if enabled. Refresh database queries.

---

## 💡 Best Practices

### For Superadmins
1. **Regular monitoring** — Check dashboard weekly for anomalies
2. **Backup before delete** — Always backup data before deleting restaurants
3. **Communication** — Notify restaurants before deactivation
4. **Documentation** — Keep notes on admin actions taken

---

<p align="center">
  <a href="../README.md">Back to Main Documentation</a>
</p>
