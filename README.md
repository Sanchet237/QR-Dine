<div align="center">
  <img src="static/images/Logo.png" alt="QRDine Logo" width="200" style="margin-bottom: 20px;"/>
  
  <h1>🍽️ QRDine — Digital Menu Platform</h1>
  
  <p>
    <em>Transform your restaurant menu into an interactive digital experience accessible via QR code</em>
  </p>
  
  <p>
    <a href="#-quick-start">Quick Start</a> •
    <a href="#-demo-credentials">Demo Credentials</a> •
    <a href="#-features">Features</a> •
    <a href="#-installation">Installation</a> •
    <a href="#-documentation">Documentation</a>
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Django-4.2.11-green?logo=django" alt="Django">
    <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">
    <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
    <img src="https://img.shields.io/badge/Status-Production%20Ready-success" alt="Status">
  </p>
  
  <img src="static/Mocup UI/Landing Page .png" alt="QRDine Landing Page" width="100%" style="margin-top: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Quick Start](#-quick-start)
- [Demo Credentials](#-demo-credentials)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Documentation](#-documentation)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**QRDine** is a production-ready, multi-tenant SaaS platform that empowers restaurants to create and manage digital menus accessible via QR codes. No app installation required for customers, no technical knowledge needed for restaurant owners.

<div align="center">
  
### 🎯 Perfect For

| 🏨 **Restaurants** | ☕ **Cafes** | 🍕 **Food Trucks** | 🍺 **Bars** |
|:---:|:---:|:---:|:---:|
| Full-service dining | Quick-service cafes | Mobile vendors | Drink menus |

</div>

**Live Demo:** [https://qr-dine-15cf.onrender.com](https://qr-dine-15cf.onrender.com)

---

### ✨ Why Choose QRDine?

<div align="center">

| Feature | Benefit |
|---------|---------|
| 🚀 **5-Minute Setup** | From registration to live menu in under 5 minutes |
| 💰 **₹0 to Start** | Free tier available, no credit card required |
| 📱 **Zero App Required** | Customers just scan and browse—no downloads |
| 🔄 **Real-Time Updates** | Mark items unavailable instantly, reflects immediately |
| 🌐 **Multi-Tenant Ready** | One platform, unlimited restaurants |
| 📊 **Analytics Ready** | Built-in dashboard with key metrics |
| 🎨 **Mobile-First Design** | Optimized for smartphones and tablets |
| 🔒 **Secure & Reliable** | Django-powered backend with role-based authentication |

</div>

---

## ⚡ Quick Start

<div align="center">

### Get QRDine running locally in 5 minutes

</div>

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Sanchet237/qrdine.git
cd qrdine

# 2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Setup database
python manage.py migrate

# 5️⃣ Create superuser (optional)
python manage.py createsuperuser

# 6️⃣ Run development server
python manage.py runserver
```

<div align="center">

🎉 **Success!** Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** to see the application.

📚 **Next Steps:** See [Installation](#-installation) for detailed setup instructions.

</div>

---

## 🔑 Demo Credentials

<div align="center">

### 🎭 Try QRDine with pre-configured demo accounts

</div>

<table align="center">
<tr>
<td width="50%" valign="top">

#### 🔐 Super Admin Access
**Platform Administration Panel**

```
URL:      https://qr-dine-15cf.onrender.com/superadmin/
Email:    admin@qrdine.com
Password: admin123
```

**What you can do:**
- ✅ View platform statistics
- ✅ Manage all restaurants
- ✅ Monitor user activity
- ✅ Toggle restaurant status
- ✅ Delete inactive restaurants

</td>
<td width="50%" valign="top">

#### 🏨 Restaurant Owner — Hotel Subedar
**Restaurant Dashboard & Menu Management**

```
URL:      https://qr-dine-15cf.onrender.com/restaurants/dashboard/
Email:    hotelsubedar@example.com
Password: subedar@123
```

**What you can do:**
- ✅ Manage menu items & categories
- ✅ Toggle item availability
- ✅ Upload dish images
- ✅ Download QR code
- ✅ View dashboard analytics

**🍽️ View Public Menu:** [https://qr-dine-15cf.onrender.com/menu/hotel-subedar/](https://qr-dine-15cf.onrender.com/menu/hotel-subedar/)

</td>
</tr>
</table>

> **💡 Tip:** These demo accounts are created automatically when you run the management commands included in the project. See [restaurants/management/commands/](restaurants/management/commands/) for details.

---

## 🎯 Problem Statement

Traditional physical menus face several challenges:
- **Costly to update**: Reprinting menus for price changes or new items is expensive
- **Unhygienic**: Shared menus pose sanitation concerns, especially post-pandemic
- **Static experience**: No real-time availability updates (sold-out items)
- **Limited information**: Space constraints restrict detailed descriptions and images
- **Language barriers**: Difficult to offer multi-language support

## 💡 Solution

QRDine is a **multi-tenant SaaS platform** that enables restaurants to digitize their menus instantly. Customers scan a QR code and access a mobile-optimized menu without installing any app. Restaurant owners manage their menus through an intuitive dashboard with real-time updates.

**Key Benefits:**
- ✅ Instant menu updates without reprinting
- ✅ Contactless ordering experience
- ✅ Rich media support (HD images, descriptions)
- ✅ Real-time availability toggles
- ✅ Analytics-ready architecture
- ✅ Zero app installation for customers

---

## ⚡ Features at a Glance

<div align="center">

| 🏪 **Restaurant Owners** | 📱 **Customers** | 🔐 **Platform Admins** |
|:---|:---|:---|
| 📝 Self-service registration | 📲 No app installation needed | 🎛️ Full platform control |
| 🍽️ Visual menu builder | 🔍 Real-time search | 👥 User management |
| 📸 Image upload & management | 🏷️ Smart category filters | 📊 Analytics dashboard |
| 📱 QR code auto-generation | 🌿 Vegan/non-veg indicators | 🗑️ Bulk operations |
| 🔄 Real-time availability toggle | 💰 Clear pricing display | 🛡️ Security controls |
| 📊 Dashboard with analytics | 🎨 Mobile-first UI/UX | 🔧 Platform configuration |
| 🎨 Restaurant profile customization | 🚀 Fast, smooth browsing | 📈 Growth monitoring |
| 🖼️ Logo & branding upload | ✅ No registration required | ⚙️ Settings management |

</div>

---

## ✨ Features

### For Restaurant Owners
- 🏪 **Self-Service Registration** — Restaurant owners can sign up and onboard independently
- 📝 **Menu Builder** — Create categories and menu items with images, descriptions, and prices
- 🔄 **Real-Time Availability Toggle** — Mark items as sold-out instantly (reflects immediately on customer menus)
- 🖼️ **Image Management** — Upload high-quality dish images with automatic optimization
- 📱 **QR Code Generation** — Auto-generated scannable QR codes for each restaurant
- 📊 **Dashboard Analytics** — View total items, available items, and sold-out count
- 🎨 **Profile Customization** — Update restaurant name, address, description, and logo

### For Customers
- 📲 **No App Required** — Access menus directly via QR scan (mobile browser)
- 🎨 **Modern UI/UX** — Dark theme with smooth animations and responsive design
- 🔍 **Advanced Search** — Real-time search across all menu items
- 🏷️ **Smart Filters**:
  - Filter by category (Starters, Main Course, Desserts, etc.)
  - Dietary filters (Veg Only / Non-Veg Only)
  - Availability filter (Hide sold-out items)
- 🌿 **Visual Dietary Indicators** — Green dot for veg, red triangle for non-veg
- 💰 **Clear Pricing** — Prices displayed in local currency

### For Platform Admins (Super Admin)
- 🔐 **Restaurant Management** — Approve/suspend restaurants
- 👥 **User Management** — View and manage restaurant admin accounts
- 📈 **Platform Dashboard** — Overview of total restaurants and activity
- 🗑️ **Bulk Operations** — Delete inactive restaurants

---

## 🛠️ Technology Stack

<div align="center">

### Backend
![Django](https://img.shields.io/badge/Django-4.2.11-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Development-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Production-316192?style=for-the-badge&logo=postgresql&logoColor=white)

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

### Libraries & Tools
![Pillow](https://img.shields.io/badge/Pillow-10.3.0-FFD43B?style=for-the-badge)
![QR Code](https://img.shields.io/badge/QR_Code-7.4.2-000000?style=for-the-badge)
![WhiteNoise](https://img.shields.io/badge/WhiteNoise-6.6.0-lightgrey?style=for-the-badge)

</div>

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend Framework** | Django 4.2.11 (Python 3.10+) | Web framework, ORM, authentication |
| **Database (Dev)** | SQLite3 | Lightweight development database |
| **Database (Prod)** | PostgreSQL | Production-ready relational database |
| **Frontend** | Django Templates + Vanilla JS | Server-side rendering with progressive enhancement |
| **Styling** | Tailwind CSS (CDN) | Utility-first CSS framework |
| **Image Processing** | Pillow 10.3.0 | Image uploads, optimization, resizing |
| **QR Generation** | qrcode[pil] 7.4.2 | Dynamic QR code generation |
| **Static Files** | WhiteNoise 6.6.0 | Static file serving in production |
| **Environment** | python-dotenv 1.0.0 | Environment variable management |
| **WSGI Server** | Gunicorn | Production HTTP server |

---

## 🏗️ System Architecture

```
┌─────────────┐
│   Customer  │ ──> Scans QR Code ──> Mobile Menu Viewer
└─────────────┘                       (Public, No Login)
                                              │
                                              ▼
┌──────────────┐                    ┌────────────────┐
│ Restaurant   │ ──> Dashboard ──>  │  Django Backend│
│    Owner     │     (CRUD Menu)    │   (Business    │
└──────────────┘                    │     Logic)     │
                                    └────────────────┘
┌──────────────┐                             │
│ Super Admin  │ ──> Admin Panel ──>         │
└──────────────┘    (Platform Mgmt)          ▼
                                    ┌────────────────┐
                                    │   SQLite DB    │
                                    │  (Models:      │
                                    │   Restaurant,  │
                                    │   MenuItem,    │
                                    │   Category)    │
                                    └────────────────┘
```

**Data Flow:**
1. Restaurant owner registers → Creates account
2. Adds menu items → Stored in database
3. QR code auto-generated → Links to `/menu/<restaurant-slug>/`
4. Customer scans QR → Fetches live menu data
5. Owner toggles availability → Updates reflected instantly

---

## 📁 Project Structure

```
qrdine/
├── accounts/                 # User authentication & authorization
│   ├── models.py            # Custom User model (roles: superadmin, restaurant_admin)
│   ├── views.py             # Login, registration, logout views
│   ├── forms.py             # Registration and login forms
│   └── urls.py              # Auth routes
│
├── restaurants/              # Restaurant management core
│   ├── models.py            # Restaurant, Category, MenuItem models
│   ├── views.py             # Dashboard, menu CRUD, QR generation
│   ├── utils.py             # QR code generation utility
│   ├── forms.py             # Menu item and category forms
│   ├── decorators.py        # @restaurant_required decorator
│   ├── context_processors.py # Global template context
│   └── management/
│       └── commands/        # CLI commands (create demo data)
│
├── menu/                     # Public menu viewer (customer-facing)
│   ├── views.py             # menu_viewer() - public menu display
│   └── urls.py              # /menu/<slug>/ route
│
├── superadmin/               # Platform administration
│   ├── views.py             # Platform dashboard, restaurant management
│   ├── decorators.py        # @superadmin_required decorator
│   └── urls.py              # /superadmin/ routes
│
├── core/                     # Landing page & shared utilities
│   ├── views.py             # Landing page, 404/500 handlers
│   └── urls.py              # Root URL
│
├── templates/                # HTML templates
│   ├── base.html            # Base template with nav
│   ├── base_dashboard.html  # Dashboard-specific base
│   ├── accounts/            # Login, registration pages
│   ├── restaurants/         # Dashboard templates
│   ├── menu/                # Public menu viewer
│   ├── superadmin/          # Admin templates
│   └── core/                # Landing page
│
├── static/                   # Static assets
│   ├── images/              # Logo, branding assets
│   └── qr_codes/            # Generated QR codes (static copy)
│
├── media/                    # User-uploaded files
│   ├── logos/               # Restaurant logos
│   ├── menu_items/          # Dish images
│   └── qr_codes/            # Generated QR codes
│
├── qrdine/                   # Django project settings
│   ├── settings.py          # Configuration
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI entry point
│
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
└── README.md                # This file
```

---

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Sanchet237/qrdine.git
cd qrdine
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies installed:**
- Django==4.2.11
- Pillow==10.3.0
- qrcode[pil]==7.4.2
- whitenoise==6.6.0
- python-dotenv==1.0.0

### Step 4: Environment Configuration

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and update:

```env
SECRET_KEY=your-super-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 5: Database Setup

```bash
# Run migrations in order
python manage.py makemigrations accounts
python manage.py migrate accounts
python manage.py makemigrations restaurants
python manage.py migrate restaurants
python manage.py migrate
```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

**Important:** When prompted for role, enter `superadmin`

### Step 7: Run Development Server

```bash
python manage.py runserver
```

Access the application at: **http://127.0.0.1:8000/**

---

## 📱 Usage Guide

### For Restaurant Owners

#### 1. Register Your Restaurant
- Navigate to `/accounts/register/`
- Fill in restaurant details (name, email, phone, address)
- Create account credentials
- Automatic slug generation from restaurant name

#### 2. Login to Dashboard
- Go to `/accounts/login/`
- Enter credentials
- Redirects to `/dashboard/`

#### 3. Manage Menu Categories
- Navigate to **Dashboard → Categories**
- Add categories (e.g., "Starters", "Main Course", "Desserts")
- Set display order (items will be sorted accordingly)

#### 4. Add Menu Items
- Go to **Dashboard → Menu Items → Add New Item**
- Fill in details:
  - Name, Description, Price
  - Upload dish image (optional)
  - Select category
  - Mark as Vegetarian (checkbox)
  - Set availability (default: available)

#### 5. Toggle Availability
- From menu items list, click **Toggle Availability** button
- Instantly marks items as sold-out or available
- Updates reflect immediately on customer menu

#### 6. Generate QR Code
- Navigate to **Dashboard → QR Code**
- QR code auto-generated linking to `/menu/<your-restaurant-slug>/`
- Download high-resolution QR code
- Print and display at tables, counter, or entrance

### For Customers

1. **Scan QR Code** at restaurant (using phone camera)
2. **Browser opens** menu automatically (no app install)
3. **Browse menu** with categories, images, and prices
4. **Use filters**:
   - Search by dish name
   - Filter by category
   - Show only Veg/Non-Veg items
   - Hide sold-out items
5. **Visual indicators**: Green dot (veg), Red triangle (non-veg)

### For Super Admins

- Access `/superadmin/` after logging in as superadmin
- View all registered restaurants
- Toggle restaurant active/inactive status
- Delete restaurants (with confirmation)
- View platform statistics

---

## 📸 Screenshots

### 🏠 Landing Page
Beautiful, modern landing page with clear call-to-actions and feature highlights.

<p align="center">
  <img src="static/Mocup UI/Landing Page .png" alt="QRDine Landing Page" width="100%" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
</p>

---

### ✍️ Restaurant Registration
Simple, streamlined registration process for restaurant owners.

<p align="center">
  <img src="static/Mocup UI/Signup Page.png" alt="Restaurant Registration" width="100%" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
</p>

---

### 📊 Restaurant Dashboard
Intuitive dashboard with menu management, analytics, and quick actions.

<p align="center">
  <img src="static/Mocup UI/Restarant Dash Board.png" alt="Restaurant Dashboard" width="100%" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
</p>

---

### 📱 QR Code Generation
Auto-generated QR codes ready to download and print for table placement.

<p align="center">
  <img src="static/Mocup UI/Restarant QR.png" alt="QR Code Generation" width="100%" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
</p>

---

### 🍽️ Customer Menu View
Mobile-optimized menu with beautiful dish images and clear pricing.

<p align="center">
  <img src="static/Mocup UI/Customer Menu.png" alt="Customer Menu View" width="60%" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
</p>

---

### 🔍 Menu with Filters
Advanced filtering by category, dietary preferences, and availability.

<p align="center">
  <img src="static/Mocup UI/Customer Filter Menu.png" alt="Menu Filters" width="60%" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
</p>

---

## 🔮 Future Enhancements

- [ ] **Online Ordering** — Add to cart and place orders
- [ ] **Payment Integration** — Razorpay/Stripe integration
- [ ] **Multi-Language Support** — Hindi, Spanish, French menus
- [ ] **Analytics Dashboard** — Track popular items, peak hours
- [ ] **Table Management** — QR codes per table with table numbers
- [ ] **Customer Reviews** — Rating and feedback system
- [ ] **Allergen Information** — Tag items with allergen warnings
- [ ] **Spice Level Indicators** — Mild, Medium, Hot labels
- [ ] **Combo Offers** — Bundle pricing and meal deals
- [ ] **Push Notifications** — Alert customers about new dishes
- [ ] **WhatsApp Integration** — Order via WhatsApp Business API
- [ ] **Dark/Light Theme Toggle** — User preference for menu theme

---

## 📚 Documentation

Detailed documentation is available for each module:

- **[Accounts Module](accounts/README.md)** — User authentication, registration, and role management
- **[Restaurants Module](restaurants/README.md)** — Core business logic, menu management, QR generation
- **[Menu Module](menu/README.md)** — Public menu viewer for customers
- **[Super Admin Module](superadmin/README.md)** — Platform administration and management
- **[Core Module](core/README.md)** — Landing page and shared utilities

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide for Python code
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Sanchet Kolekar

---

## 👨‍💻 Author

<div align="center">

### Sanchet Kolekar

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sanchet%20Kolekar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sanchet-kolekar-613916331/)
[![Instagram](https://img.shields.io/badge/Instagram-@sanchetkolekar-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/sanchetkolekar/)
[![GitHub](https://img.shields.io/badge/GitHub-Sanchet237-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Sanchet237)
[![Email](https://img.shields.io/badge/Email-Sanchetkolekar.07%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Sanchetkolekar.07@gmail.com)
[![Phone](https://img.shields.io/badge/Phone-7066062254-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](tel:+917066062254)
[![Project](https://img.shields.io/badge/Project-QRDine%20Repo-054D3A?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Sanchet237/qrdine)

</div>

---

## ⭐ Show Your Support

If you find QRDine useful, please consider:

- ⭐ Starring this repository
- 🐛 Reporting bugs or suggesting features via [Issues](https://github.com/Sanchet237/qrdine/issues)
- 🔀 Contributing to the codebase via [Pull Requests](https://github.com/Sanchet237/qrdine/pulls)
- 📣 Sharing with restaurant owners who could benefit

---

<div align="center">

<img src="static/images/Logo.png" alt="QRDine Logo" width="80"/>

### Made with ❤️ for the restaurant industry

**Transforming dining experiences, one QR code at a time**

---

<sub>© 2026 Sanchet Kolekar. Licensed under MIT.</sub>

[![Django](https://img.shields.io/badge/Built_with-Django-092E20?style=flat&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Powered_by-Python-3776AB?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)](LICENSE)

</div>
