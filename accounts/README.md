# 👤 Accounts Module

This module handles user authentication, registration, and role-based access control for the QRDine platform.

---

## 📋 Overview

The accounts module provides:
- User registration with role assignment
- Login/logout functionality
- Custom user model with role-based permissions
- Restaurant admin and superadmin role management

---

## 🏗️ Architecture

### Models

#### CustomUser (`models.py`)
```python
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('restaurant_admin', 'Restaurant Admin'),
        ('superadmin', 'Super Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True, null=True)
```

**Fields:**
- `role` — User role (restaurant_admin or superadmin)
- `phone` — Contact phone number
- Inherits from Django's `AbstractUser` (username, email, password, etc.)

---

## 🔐 Authentication Flow

```
Registration Flow:
┌─────────────────┐
│  User visits    │
│  /register/     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Fill form:     │
│  - Username     │
│  - Email        │
│  - Password     │
│  - Phone        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  User created   │
│  Role: admin    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Auto-login     │
│  Redirect to    │
│  Dashboard      │
└─────────────────┘
```

---

## 📁 File Structure

```
accounts/
├── __init__.py
├── admin.py           # Django admin configuration
├── apps.py            # App configuration
├── forms.py           # Registration and login forms
├── models.py          # CustomUser model
├── tests.py           # Unit tests
├── urls.py            # URL routing
├── views.py           # View functions
└── migrations/        # Database migrations
    ├── __init__.py
    └── 0001_initial.py
```

---

## 🔗 URL Routes

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/accounts/register/` | `register_view` | User registration page |
| `/accounts/login/` | `login_view` | User login page |
| `/accounts/logout/` | `logout_view` | User logout |

---

## 📝 Forms

### RegistrationForm (`forms.py`)
```python
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']
```

### LoginForm (`forms.py`)
```python
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
```

---

## 🎨 Views

### `register_view(request)`
- **Method:** GET, POST
- **Template:** `accounts/register.html`
- **Logic:**
  - GET: Display registration form
  - POST: Validate form, create user with `restaurant_admin` role, auto-login
- **Redirects:** `/dashboard/` on success

### `login_view(request)`
- **Method:** GET, POST
- **Template:** `accounts/login.html`
- **Logic:**
  - GET: Display login form
  - POST: Authenticate user, login if valid
- **Redirects:** 
  - Superadmin → `/superadmin/`
  - Restaurant admin → `/dashboard/`

### `logout_view(request)`
- **Method:** GET
- **Logic:** Logout user and clear session
- **Redirects:** `/accounts/login/`

---

## 🔧 Configuration

### Settings Required

Add to `qrdine/settings.py`:

```python
# Custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Login/logout URLs
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
```

---

## 🧪 Testing

Run tests:
```bash
python manage.py test accounts
```

Example test cases:
- User registration creates user with correct role
- Login redirects based on user role
- Invalid credentials return error
- Logout clears session

---

## 🛡️ Security Features

- **Password hashing:** Django's PBKDF2 algorithm
- **CSRF protection:** Enabled on all forms
- **Role-based access:** Enforced via decorators
- **Session management:** Secure session handling

---

## 🔑 Role-Based Permissions

### Restaurant Admin
- Access to own restaurant dashboard
- Cannot view other restaurants
- Cannot access superadmin panel

### Superadmin
- Access to all restaurants
- Platform-level management
- User management capabilities

---

## 📊 Database Schema

```sql
CREATE TABLE accounts_customuser (
    id INTEGER PRIMARY KEY,
    username VARCHAR(150) UNIQUE,
    email VARCHAR(254),
    password VARCHAR(128),
    phone VARCHAR(15),
    role VARCHAR(20),
    is_active BOOLEAN,
    is_staff BOOLEAN,
    is_superuser BOOLEAN,
    date_joined DATETIME,
    last_login DATETIME
);
```

---

## 🚀 Usage Example

### Register a New User

```python
from accounts.models import CustomUser

# Create restaurant admin
user = CustomUser.objects.create_user(
    username='restaurant1',
    email='owner@restaurant.com',
    password='secure_password',
    role='restaurant_admin',
    phone='+91 9876543210'
)
```

### Check User Role

```python
if request.user.role == 'superadmin':
    # Allow superadmin access
    pass
elif request.user.role == 'restaurant_admin':
    # Allow restaurant admin access
    pass
```

---

## 🔄 Future Enhancements

- [ ] Email verification for registration
- [ ] Password reset functionality
- [ ] Two-factor authentication (2FA)
- [ ] Social login (Google, Facebook)
- [ ] User profile management
- [ ] Account deactivation/deletion

---

## 📚 Related Modules

- **[Restaurants](../restaurants/README.md)** — Uses authentication for dashboard access
- **[Superadmin](../superadmin/README.md)** — Requires superadmin role
- **[Core](../core/README.md)** — Landing page with login/register links

---

## 🆘 Troubleshooting

### Issue: "AUTH_USER_MODEL" error
**Solution:** Ensure `AUTH_USER_MODEL = 'accounts.CustomUser'` is in settings.py before running migrations.

### Issue: Migration conflicts
**Solution:**
```bash
python manage.py makemigrations accounts
python manage.py migrate accounts
```

### Issue: Login redirects to wrong page
**Solution:** Check `LOGIN_REDIRECT_URL` in settings.py and role-based redirect logic.

---

<p align="center">
  <a href="../README.md">Back to Main Documentation</a>
</p>
