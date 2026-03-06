# 🏠 Core Module

This module provides the landing page, error handlers, and shared utilities for the QRDine platform.

---

## 📋 Overview

The core module provides:
- Public landing page with product information
- Error handling (404, 500)
- Privacy policy and terms of service pages
- SEO optimization
- Marketing content

---

## 📁 File Structure

```
core/
├── __init__.py
├── admin.py          # No admin configuration
├── apps.py           # App configuration
├── models.py         # No models
├── views.py          # Landing page and error views
├── tests.py          # Unit tests
└── urls.py           # URL routing
```

---

## 🔗 URL Routes

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/` | `landing_page` | Homepage with product info |
| `/privacy/` | `privacy_policy` | Privacy policy page |
| `/terms/` | `terms_of_service` | Terms of service page |
| (handler404) | `custom_404` | Custom 404 error page |
| (handler500) | `custom_500` | Custom 500 error page |

---

## 🎨 Landing Page Structure

The landing page (`templates/core/landing.html`) includes:

### 1. Hero Section
```html
<section id="hero">
    <h1>Transform Your Restaurant Menu Into a Digital Experience</h1>
    <p>Create QR code menus in minutes. No app required for customers.</p>
    <div class="cta-buttons">
        <a href="{% url 'register' %}">Get Started Free</a>
        <a href="#how-it-works">See How It Works</a>
    </div>
</section>
```

**Features:**
- Compelling headline
- Clear value proposition
- Call-to-action buttons
- Animated gradient background

### 2. Stats Band
```html
<section id="stats">
    <div class="stat-card">
        <p>40+</p>
        <span>Restaurants registered</span>
    </div>
    <div class="stat-card">
        <p>500+</p>
        <span>Menu items live</span>
    </div>
    <div class="stat-card">
        <p><5 min</p>
        <span>To go live</span>
    </div>
    <div class="stat-card">
        <p>₹0</p>
        <span>To get started</span>
    </div>
</section>
```

### 3. Features Section
```html
<section id="features">
    <h2>Everything your restaurant needs. Nothing it doesn't.</h2>
    
    <!-- Features Grid (2x3) -->
    <div class="features-grid">
        <!-- Feature 1: Instant QR Code -->
        <div class="feature-card">
            <div class="icon"><!-- QR icon SVG --></div>
            <h4>Instant QR Code</h4>
            <p>Your QR code is ready the second you register...</p>
        </div>
        
        <!-- Feature 2-6: Similar structure -->
    </div>
</section>
```

**6 Features:**
1. **Instant QR Code** — Auto-generated on signup
2. **Real-Time Updates** — Mark items unavailable instantly
3. **Mobile-First Design** — Works on any phone
4. **Smart Categories** — Organize menu logically
5. **Photo Uploads** — Add dish images easily
6. **Contactless & Hygienic** — No shared menus

### 4. How It Works Section
```html
<section id="how-it-works">
    <h2>Up and running in four steps.</h2>
    
    <!-- Step-by-step process -->
    <div class="steps-grid">
        <div class="step">
            <div class="step-number">01</div>
            <h3>Register Free</h3>
            <p>Sign up with restaurant details. Takes under 2 minutes.</p>
        </div>
        
        <!-- Steps 2-4: Add Menu, Get QR, Go Live -->
    </div>
</section>
```

### 5. About Section
```html
<section id="about">
    <div class="about-content">
        <h2>Built for the restaurant owner, not the IT team.</h2>
        <p>QRDine was born from a simple frustration...</p>
    </div>
    <div class="about-image">
        <!-- Illustration or screenshot -->
    </div>
</section>
```

### 6. Testimonials (Optional)
```html
<section id="testimonials">
    <h2>What restaurant owners say</h2>
    
    <div class="testimonial-card">
        <p>"QRDine helped us go digital in under an hour. Our customers love it!"</p>
        <span>— Owner, Cafe Delight</span>
    </div>
</section>
```

### 7. CTA Section
```html
<section id="cta">
    <h2>Ready to digitize your menu?</h2>
    <p>Join 40+ restaurants already using QRDine</p>
    <a href="{% url 'register' %}" class="cta-button">Start Free Today</a>
</section>
```

### 8. Footer
```html
<footer>
    <div class="footer-content">
        <div class="footer-column">
            <h4>Product</h4>
            <ul>
                <li><a href="#features">Features</a></li>
                <li><a href="#how-it-works">How It Works</a></li>
                <li><a href="{% url 'register' %}">Sign Up</a></li>
            </ul>
        </div>
        
        <div class="footer-column">
            <h4>Company</h4>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="{% url 'privacy' %}">Privacy Policy</a></li>
                <li><a href="{% url 'terms' %}">Terms of Service</a></li>
            </ul>
        </div>
        
        <div class="footer-column">
            <h4>Support</h4>
            <ul>
                <li><a href="mailto:support@qrdine.com">Contact</a></li>
            </ul>
        </div>
    </div>
    
    <div class="footer-bottom">
        <p>© 2026 QRDine. All rights reserved.</p>
    </div>
</footer>
```

---

## 🎨 Design Elements

### Color Palette
```css
:root {
    --primary-green: #10B981;
    --dark-green: #054D3A;
    --light-green: #DCFCE7;
    --cream: #F9F7F3;
    --dark: #0D0D0D;
    --gray: #6B7280;
}
```

### Typography
- **Headings:** 'Instrument Serif' (serif font)
- **Body:** System fonts (San Francisco, Segoe UI, Roboto)
- **Monospace:** 'DM Mono' (for code/technical text)

### Decorative Elements
- **Floating QR codes** — Subtle background patterns (opacity: 0.03-0.04)
- **Wave dividers** — SVG waves between sections
- **Gradient backgrounds** — Smooth color transitions
- **Hover effects** — Card lifts, shadow animations

---

## 🔍 SEO Optimization

### Meta Tags
```html
<head>
    <title>QRDine — Digital QR Code Menus for Restaurants</title>
    <meta name="description" content="Create digital menus with QR codes in minutes. No app required. Free to start. Perfect for restaurants, cafes, and bistros.">
    <meta name="keywords" content="QR code menu, digital menu, restaurant menu, contactless menu, online menu">
    
    <!-- Open Graph -->
    <meta property="og:title" content="QRDine — Digital Menu Platform">
    <meta property="og:description" content="Transform your restaurant menu into a digital experience">
    <meta property="og:image" content="{% static 'images/og-image.png' %}">
    <meta property="og:url" content="https://qrdine.com">
    <meta property="og:type" content="website">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="QRDine — Digital Menu Platform">
    <meta name="twitter:description" content="Create QR code menus in minutes">
    <meta name="twitter:image" content="{% static 'images/twitter-card.png' %}">
</head>
```

### Structured Data (JSON-LD)
```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "QRDine",
    "applicationCategory": "BusinessApplication",
    "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
    },
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "ratingCount": "42"
    }
}
</script>
```

---

## 📄 Legal Pages

### Privacy Policy (`templates/core/privacy.html`)

Sections:
1. Information We Collect
2. How We Use Your Information
3. Data Security
4. Third-Party Services
5. User Rights
6. Cookie Policy
7. Children's Privacy
8. Changes to Policy
9. Contact Information

### Terms of Service (`templates/core/terms.html`)

Sections:
1. Acceptance of Terms
2. Service Description
3. User Accounts
4. User Responsibilities
5. Intellectual Property
6. Payment Terms (if applicable)
7. Service Availability
8. Limitation of Liability
9. Termination
10. Governing Law

---

## ⚠️ Error Handlers

### Custom 404 Page (`templates/404.html`)

```html
<div class="error-page">
    <h1>404</h1>
    <h2>Page Not Found</h2>
    <p>The page you're looking for doesn't exist or has been moved.</p>
    <a href="{% url 'landing' %}">Go back home</a>
</div>
```

**When triggered:**
- Invalid URL accessed
- Restaurant slug not found
- Deleted resource accessed

### Custom 500 Page (`templates/500.html`)

```html
<div class="error-page">
    <h1>500</h1>
    <h2>Server Error</h2>
    <p>Something went wrong on our end. We're working to fix it.</p>
    <a href="{% url 'landing' %}">Go back home</a>
</div>
```

**When triggered:**
- Unhandled exceptions
- Database connection errors
- Server-side errors

---

## 🔧 View Functions

### `landing_page(request)` (`views.py`)
```python
def landing_page(request):
    """
    Display public landing page
    """
    context = {
        'total_restaurants': Restaurant.objects.filter(is_active=True).count(),
        'total_items': MenuItem.objects.filter(is_available=True).count(),
    }
    return render(request, 'core/landing.html', context)
```

### `privacy_policy(request)`
```python
def privacy_policy(request):
    """
    Display privacy policy page
    """
    return render(request, 'core/privacy.html')
```

### `terms_of_service(request)`
```python
def terms_of_service(request):
    """
    Display terms of service page
    """
    return render(request, 'core/terms.html')
```

### `custom_404(request, exception)`
```python
def custom_404(request, exception):
    """
    Custom 404 error handler
    """
    return render(request, '404.html', status=404)
```

### `custom_500(request)`
```python
def custom_500(request):
    """
    Custom 500 error handler
    """
    return render(request, '500.html', status=500)
```

---

## 📱 Responsive Design

### Breakpoints
```css
/* Mobile: < 768px */
@media (max-width: 767px) {
    .features-grid {
        grid-template-columns: 1fr;
    }
}

/* Tablet: 768px - 1024px */
@media (min-width: 768px) and (max-width: 1024px) {
    .features-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Desktop: > 1024px */
@media (min-width: 1025px) {
    .features-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

---

## 🚀 Performance Optimization

### Image Optimization
- Use WebP format with PNG fallback
- Lazy loading for below-the-fold images
- Responsive images with `srcset`

```html
<img 
    src="{% static 'images/feature-small.webp' %}"
    srcset="
        {% static 'images/feature-small.webp' %} 480w,
        {% static 'images/feature-medium.webp' %} 768w,
        {% static 'images/feature-large.webp' %} 1200w
    "
    loading="lazy"
    alt="Feature description"
>
```

### CSS Optimization
- Inline critical CSS
- Defer non-critical CSS
- Minify stylesheets in production

### JavaScript Optimization
- Minimize JavaScript usage (vanilla JS only)
- Defer script loading
- Compress JavaScript files

---

## 📊 Analytics Integration (Future)

### Google Analytics
```html
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Tracking Events
- **Registration clicks** — Track "Get Started" button
- **Section views** — Track scroll depth (features, how it works)
- **External links** — Track clicks to social media

---

## 🔄 Future Enhancements

- [ ] Blog section for SEO
- [ ] Customer testimonials slider
- [ ] Video demo/walkthrough
- [ ] Live chat support widget
- [ ] Multi-language support
- [ ] A/B testing different headlines
- [ ] Interactive pricing calculator

---

## 📚 Related Modules

- **[Accounts](../accounts/README.md)** — Registration/login linked from landing
- **[Restaurants](../restaurants/README.md)** — Demo menu links
- **[Menu](../menu/README.md)** — Public menu viewer

---

## 🆘 Troubleshooting

### Issue: Static files not loading
**Solution:** Run `python manage.py collectstatic` and verify `STATIC_URL` in settings.

### Issue: Images not displaying
**Solution:** Check `MEDIA_URL` and ensure media folder exists.

### Issue: 404/500 pages not showing
**Solution:** Set `DEBUG=False` in settings.py and add custom error handlers in urls.py.

---

## 💡 Content Writing Tips

### Headlines
- Use action verbs: "Transform", "Create", "Build"
- Focus on benefits, not features
- Keep it concise (under 10 words)

### Call-to-Action
- Use urgent language: "Start Free Today", "Get Started Now"
- Eliminate friction: "No credit card required"
- Create FOMO: "Join 40+ restaurants"

### Value Proposition
- Lead with the problem: "Tired of reprinting menus?"
- Present the solution: "QRDine solves this with..."
- Show the outcome: "Save time and money"

---

<p align="center">
  <a href="../README.md">Back to Main Documentation</a>
</p>
