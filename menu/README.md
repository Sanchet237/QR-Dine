# 📱 Menu Module

This module provides the public-facing menu viewer that customers see when they scan the QR code. No authentication required.

---

## 📋 Overview

The menu module provides:
- Public menu viewer (no login required)
- Real-time menu data from database
- Advanced filtering and search
- Mobile-optimized interface
- Dietary indicators (veg/non-veg)

---

## 🏗️ Architecture

### Views

#### `menu_viewer(request, slug)` (`views.py`)
- **Method:** GET
- **Template:** `menu/viewer.html`
- **Authentication:** Not required (public access)
- **Logic:**
  - Fetch restaurant by slug
  - Check if restaurant is active
  - Retrieve all menu items with categories
  - Group items by category
  - Display with filters and search

---

## 📁 File Structure

```
menu/
├── __init__.py
├── admin.py          # Django admin configuration (minimal)
├── apps.py           # App configuration
├── models.py         # No models (uses restaurants models)
├── views.py          # menu_viewer() view
├── tests.py          # Unit tests
└── urls.py           # URL routing
```

---

## 🔗 URL Routes

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/menu/<slug>/` | `menu_viewer` | Public menu for restaurant |

**Example:**
- `/menu/hotel-subedar/` → Shows menu for Hotel Subedar
- `/menu/pizza-palace/` → Shows menu for Pizza Palace

---

## 🎨 View Logic

### Menu Viewer Flow

```
1. Customer scans QR code
2. Browser opens /menu/<restaurant-slug>/
3. View fetches restaurant by slug
4. Check if restaurant is active
   ├─ Yes: Display menu
   └─ No: Show "unavailable" page
5. Fetch all menu items with categories
6. Group items by category (ordered by display_order)
7. Render menu with filters
```

### Data Structure Passed to Template

```python
context = {
    'restaurant': restaurant_object,
    'categories': [
        {
            'category': category_object,
            'items': [item1, item2, item3...]
        },
        ...
    ]
}
```

---

## 🧭 Features

### 1. Real-Time Search
```javascript
// Searches item name and description
<input type="text" id="searchInput" placeholder="Search menu...">
```

### 2. Category Filter
```html
<!-- Dropdown to filter by category -->
<select id="categoryFilter">
    <option value="">All Categories</option>
    <option value="starters">Starters</option>
    <option value="main-course">Main Course</option>
</select>
```

### 3. Dietary Filters
```html
<!-- Filter veg/non-veg items -->
<button id="vegOnly">Veg Only</button>
<button id="nonVegOnly">Non-Veg Only</button>
<button id="showAll">Show All</button>
```

### 4. Availability Filter
```html
<!-- Hide sold-out items -->
<label>
    <input type="checkbox" id="hideUnavailable">
    Hide Sold Out Items
</label>
```

---

## 🎨 UI Components

### Menu Card Structure

```html
<div class="menu-item" data-veg="true" data-available="true">
    <!-- Item image -->
    <img src="{{ item.image.url }}" alt="{{ item.name }}">
    
    <!-- Veg/Non-veg indicator -->
    <span class="dietary-badge">
        {% if item.is_vegetarian %}
            <span class="veg-dot">●</span> Veg
        {% else %}
            <span class="non-veg-triangle">▲</span> Non-Veg
        {% endif %}
    </span>
    
    <!-- Item details -->
    <h3>{{ item.name }}</h3>
    <p>{{ item.description }}</p>
    <span class="price">₹{{ item.price }}</span>
    
    <!-- Availability badge -->
    {% if not item.is_available %}
        <span class="sold-out-badge">Sold Out</span>
    {% endif %}
</div>
```

---

## 🔄 JavaScript Functionality

### Search Implementation

```javascript
document.getElementById('searchInput').addEventListener('input', function(e) {
    const searchTerm = e.target.value.toLowerCase();
    const items = document.querySelectorAll('.menu-item');
    
    items.forEach(item => {
        const name = item.dataset.name.toLowerCase();
        const description = item.dataset.description.toLowerCase();
        
        if (name.includes(searchTerm) || description.includes(searchTerm)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
});
```

### Filter Implementation

```javascript
function filterItems(filters) {
    const items = document.querySelectorAll('.menu-item');
    
    items.forEach(item => {
        let show = true;
        
        // Category filter
        if (filters.category && item.dataset.category !== filters.category) {
            show = false;
        }
        
        // Dietary filter
        if (filters.dietary === 'veg' && item.dataset.veg !== 'true') {
            show = false;
        }
        
        // Availability filter
        if (filters.hideUnavailable && item.dataset.available === 'false') {
            show = false;
        }
        
        item.style.display = show ? 'block' : 'none';
    });
}
```

---

## 🎨 Styling

The menu viewer uses:
- **Dark theme** — Modern, elegant look
- **Card-based layout** — Each item in a card
- **Grid system** — Responsive 2-3 column layout
- **Smooth animations** — Fade in/out on filter changes
- **Mobile-first** — Touch-friendly, optimized for phones

---

## 📱 Mobile Optimization

- **Touch-friendly buttons** — Large tap targets
- **Swipe gestures** — Horizontal category scroll
- **Optimized images** — Lazy loading, compressed
- **Fast loading** — Minimal JavaScript, CSS
- **Progressive enhancement** — Works without JS

---

## 🔒 Error Handling

### Restaurant Not Found (404)
```python
try:
    restaurant = Restaurant.objects.get(slug=slug, is_active=True)
except Restaurant.DoesNotExist:
    return render(request, 'menu/unavailable.html', status=404)
```

### Restaurant Inactive
```html
<!-- menu/unavailable.html -->
<div class="unavailable-message">
    <h1>Menu Not Available</h1>
    <p>This restaurant's menu is currently unavailable.</p>
    <p>Please contact the restaurant for more information.</p>
</div>
```

---

## 🧪 Testing

Run tests:
```bash
python manage.py test menu
```

Test cases:
- Valid slug returns menu
- Invalid slug returns 404
- Inactive restaurant returns unavailable page
- Sold-out items are marked correctly
- Search filter works
- Category filter works

---

## 🚀 Performance Optimization

### Database Queries
```python
# Use select_related and prefetch_related
restaurant = Restaurant.objects.select_related('user').get(slug=slug)
categories = Category.objects.filter(
    restaurant=restaurant
).prefetch_related(
    Prefetch('menuitem_set', queryset=MenuItem.objects.all())
).order_by('display_order')
```

### Caching (Future)
```python
from django.core.cache import cache

def menu_viewer(request, slug):
    cache_key = f'menu_{slug}'
    menu_data = cache.get(cache_key)
    
    if not menu_data:
        # Fetch from database
        menu_data = fetch_menu_data(slug)
        cache.set(cache_key, menu_data, 300)  # Cache for 5 minutes
    
    return render(request, 'menu/viewer.html', {'menu_data': menu_data})
```

---

## 📊 Analytics (Future Enhancement)

Track user behavior:
- **View counts** — How many times menu was viewed
- **Popular items** — Most searched items
- **Peak hours** — When menu is viewed most
- **Device types** — Mobile vs desktop usage

---

## 🌐 SEO Optimization

### Meta Tags
```html
<head>
    <title>{{ restaurant.name }} - Menu</title>
    <meta name="description" content="{{ restaurant.description }}">
    <meta property="og:title" content="{{ restaurant.name }} Menu">
    <meta property="og:image" content="{{ restaurant.logo.url }}">
    <meta property="og:url" content="{{ request.build_absolute_uri }}">
</head>
```

### Structured Data (JSON-LD)
```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Restaurant",
    "name": "{{ restaurant.name }}",
    "address": "{{ restaurant.address }}",
    "telephone": "{{ restaurant.phone }}",
    "menu": "{{ request.build_absolute_uri }}"
}
</script>
```

---

## 🔄 Future Enhancements

- [ ] Multi-language menus
- [ ] Voice search support
- [ ] Add to cart functionality
- [ ] Online ordering integration
- [ ] Customer reviews and ratings
- [ ] Dish recommendations
- [ ] Allergen information display
- [ ] Nutritional facts

---

## 📚 Related Modules

- **[Restaurants](../restaurants/README.md)** — Provides menu data models
- **[Core](../core/README.md)** — Landing page links to demo menus

---

## 🆘 Troubleshooting

### Issue: Menu not displaying items
**Solution:** Check if restaurant has menu items added and `is_active=True`.

### Issue: Images not loading
**Solution:** Verify `MEDIA_URL` and `MEDIA_ROOT` in settings. Check file paths.

### Issue: Filters not working
**Solution:** Ensure JavaScript is enabled. Check browser console for errors.

### Issue: Slow loading
**Solution:** Optimize images (compress, resize). Add database indexes on `slug` field.

---

## 💡 Usage Tips

### Best Practices for Restaurant Owners
1. **Add high-quality images** — Visual appeal drives orders
2. **Write clear descriptions** — Help customers make decisions
3. **Update availability daily** — Mark sold-out items promptly
4. **Organize categories** — Use logical ordering (Starters → Mains → Desserts)
5. **Set competitive prices** — Clearly display prices

---

<p align="center">
  <a href="../README.md">Back to Main Documentation</a>
</p>
