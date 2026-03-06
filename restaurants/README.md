# 🍴 Restaurants Module

This is the core business logic module that handles restaurant profiles, menu management, categories, and QR code generation.

---

## 📋 Overview

The restaurants module provides:
- Restaurant profile management
- Menu item CRUD operations
- Category management
- QR code generation and management
- Dashboard analytics
- Real-time availability toggles

---

## 🏗️ Architecture

### Models

#### Restaurant (`models.py`)
```python
class Restaurant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    description = models.TextField(blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

#### Category (`models.py`)
```python
class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
```

#### MenuItem (`models.py`)
```python
class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    is_vegetarian = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

---

## 📁 File Structure

```
restaurants/
├── __init__.py
├── admin.py               # Django admin configuration
├── apps.py                # App configuration
├── models.py              # Restaurant, Category, MenuItem models
├── views.py               # Dashboard and CRUD views
├── forms.py               # Model forms
├── urls.py                # URL routing
├── utils.py               # QR code generation utility
├── decorators.py          # @restaurant_required decorator
├── context_processors.py  # Global context variables
├── tests.py               # Unit tests
├── management/            # Custom management commands
│   └── commands/
│       ├── create_hotel_subedar.py
│       └── generate_qr_subedar.py
└── migrations/            # Database migrations
```

---

## 🔗 URL Routes

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/dashboard/` | `dashboard` | Restaurant dashboard overview |
| `/dashboard/profile/` | `profile_view` | Update restaurant profile |
| `/dashboard/categories/` | `categories_view` | Manage categories |
| `/dashboard/menu-items/` | `menu_items_view` | View all menu items |
| `/dashboard/add-item/` | `add_item_view` | Add new menu item |
| `/dashboard/edit-item/<id>/` | `edit_item_view` | Edit menu item |
| `/dashboard/delete-item/<id>/` | `delete_item_view` | Delete menu item |
| `/dashboard/toggle-availability/<id>/` | `toggle_availability` | Toggle item availability |
| `/dashboard/qr-code/` | `qr_code_view` | View/download QR code |

---

## 🎨 Key Views

### `dashboard(request)`
- **Decorator:** `@login_required`, `@restaurant_required`
- **Template:** `restaurants/dashboard.html`
- **Logic:**
  - Display restaurant stats (total items, available, sold-out)
  - Show recent menu items
  - Quick actions (add item, manage categories)

### `add_item_view(request)`
- **Method:** GET, POST
- **Template:** `restaurants/add_item.html`
- **Logic:**
  - GET: Display form with categories dropdown
  - POST: Validate and save menu item with image
- **Redirects:** `/dashboard/menu-items/` on success

### `toggle_availability(request, item_id)`
- **Method:** POST
- **Logic:**
  - Toggle `is_available` field for menu item
  - AJAX-friendly (returns JSON response)
- **Response:** `{'status': 'success', 'is_available': boolean}`

### `qr_code_view(request)`
- **Template:** `restaurants/qr_code.html`
- **Logic:**
  - Generate QR code if not exists (calls `utils.generate_qr_code()`)
  - Display QR code with download link
  - Show public menu URL

---

## 🔧 Utilities

### QR Code Generation (`utils.py`)

```python
def generate_qr_code(restaurant):
    """
    Generate QR code for restaurant's public menu URL
    """
    import qrcode
    from io import BytesIO
    from django.core.files.base import ContentFile
    
    # Generate URL
    url = f"https://yourdomain.com/menu/{restaurant.slug}/"
    
    # Create QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to model
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    filename = f'qr_{restaurant.slug}.png'
    restaurant.qr_code.save(filename, ContentFile(buffer.getvalue()), save=True)
    
    return restaurant.qr_code.url
```

---

## 🛡️ Decorators

### `@restaurant_required` (`decorators.py`)

```python
def restaurant_required(view_func):
    """
    Decorator to ensure user has an associated restaurant
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not hasattr(request.user, 'restaurant'):
            return redirect('register')  # Or appropriate page
        return view_func(request, *args, **kwargs)
    return wrapper
```

**Usage:**
```python
@login_required
@restaurant_required
def dashboard(request):
    # View logic
    pass
```

---

## 📊 Database Relationships

```
CustomUser (accounts)
    │
    ├─── OneToOne ───> Restaurant
                           │
                           ├─── ForeignKey ───> Category
                           │                       │
                           │                       └─── ForeignKey ───> MenuItem
                           │
                           └─── ForeignKey ───> MenuItem (direct)
```

---

## 🔄 Business Logic Flow

### Restaurant Creation Flow
```
1. User registers → CustomUser created
2. Post-registration signal → Restaurant profile created
3. Auto-generate slug from restaurant name
4. QR code generation scheduled (on first access)
```

### Menu Item Management Flow
```
1. Restaurant admin adds item
2. Item saved with restaurant and category FK
3. Image uploaded to media/menu_items/
4. Item appears on public menu instantly
5. Toggle availability doesn't delete item (soft delete)
```

---

## 🎨 Forms

### RestaurantProfileForm (`forms.py`)
```python
class RestaurantProfileForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'email', 'phone', 'address', 'logo', 'description']
```

### MenuItemForm (`forms.py`)
```python
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category', 
                  'image', 'is_vegetarian', 'is_available']
```

### CategoryForm (`forms.py`)
```python
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'display_order']
```

---

## 🧪 Testing

Run tests:
```bash
python manage.py test restaurants
```

Key test cases:
- Restaurant creation on user signup
- Menu item CRUD operations
- QR code generation
- Availability toggle
- Category ordering

---

## 🚀 Management Commands

### Create Demo Restaurant
```bash
python manage.py create_hotel_subedar
```
Creates a demo restaurant "Hotel Subedar" with sample menu items.

### Generate QR Codes
```bash
python manage.py generate_qr_subedar
```
Generates QR codes for all restaurants missing them.

---

## 📈 Dashboard Analytics

The dashboard shows:
- **Total Menu Items** — Count of all items
- **Available Items** — Items with `is_available=True`
- **Sold Out Items** — Items with `is_available=False`
- **Recent Items** — Last 5 added items
- **Categories Count** — Number of categories

---

## 🔒 Access Control

- Restaurant admins can only view/edit their own restaurant
- Enforced via `@restaurant_required` decorator
- QuerySets filtered by `request.user.restaurant`
- Superadmins have full access

---

## 🔄 Future Enhancements

- [ ] Bulk menu item upload (CSV import)
- [ ] Menu versioning (track changes)
- [ ] Multi-language menu support
- [ ] Nutritional information fields
- [ ] Allergen warnings
- [ ] Dish popularity tracking
- [ ] Inventory management

---

## 📚 Related Modules

- **[Accounts](../accounts/README.md)** — User authentication
- **[Menu](../menu/README.md)** — Public menu viewer
- **[Superadmin](../superadmin/README.md)** — Platform management

---

## 🆘 Troubleshooting

### Issue: QR code not generating
**Solution:** Ensure `qrcode[pil]` and `Pillow` are installed. Check media folder permissions.

### Issue: Images not displaying
**Solution:** Verify `MEDIA_URL` and `MEDIA_ROOT` in settings.py. Ensure `media/` folder exists.

### Issue: Slug conflicts
**Solution:** Slugs are auto-generated from restaurant name. Ensure unique restaurant names.

---

<p align="center">
  <a href="../README.md">Back to Main Documentation</a>
</p>
