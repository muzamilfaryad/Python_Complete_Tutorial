# Django Web Application (src)

A comprehensive Django web application demonstrating multi-app architecture with template-based rendering.

## 📚 Overview

This project showcases a traditional Django web application with multiple interconnected apps:
- **Blog**: Blog post management and publishing
- **Courses**: Online course catalog and details
- **Pages**: Static and dynamic pages
- **Products**: Product catalog and display

## 🎯 Features

✅ Multiple Django apps  
✅ Template-based rendering  
✅ Database models and relationships  
✅ Admin interface integration  
✅ URL routing and views  
✅ Form handling and validation  
✅ Static files management  
✅ Database migrations  

## 📂 Project Structure

```
src/
├── manage.py
├── db.sqlite3
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── courses/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── pages/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│
├── products/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── contact.html
│   └── navbar.html
│
└── trydjango/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Django 3.0+
- pip

### Installation

1. Navigate to project directory:
```bash
cd src
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

**Access**: http://localhost:8000

---

## 📱 Apps Overview

### Blog App
**Purpose**: Manage and display blog posts

**Models**:
- Post: Title, content, author, publication date, categories
- Category: Blog post categories
- Comment: Reader comments on posts

**Features**:
- Create/edit/delete posts
- Categorize posts
- List posts by category
- Comment functionality
- Admin management

**URLs**:
- `/blog/` - Blog home
- `/blog/<slug>/` - Blog post detail
- `/blog/category/<slug>/` - Posts by category

---

### Courses App
**Purpose**: Display online courses

**Models**:
- Course: Title, description, instructor, price, duration
- Lesson: Course lessons/modules
- Enrollment: Student course enrollment

**Features**:
- Course catalog
- Course details
- Lesson listings
- Enrollment management
- Admin dashboard

**URLs**:
- `/courses/` - Course listing
- `/courses/<slug>/` - Course detail
- `/courses/enroll/<id>/` - Enroll in course

---

### Pages App
**Purpose**: Manage static and dynamic pages

**Models**:
- Page: Title, content, slug, metadata

**Features**:
- About page
- Contact page
- FAQ page
- Custom pages
- Easy content management

**URLs**:
- `/about/` - About page
- `/contact/` - Contact page
- `/pages/<slug>/` - Custom pages

---

### Products App
**Purpose**: Product catalog and display

**Models**:
- Product: Name, description, price, stock, category
- Category: Product categories
- Review: Product reviews and ratings

**Features**:
- Product listing
- Product details
- Search products
- Filter by category
- Product reviews
- Stock management

**URLs**:
- `/products/` - Product listing
- `/products/<slug>/` - Product detail
- `/products/category/<slug>/` - Products by category

---

## 🛠️ Common Management Commands

```bash
# Run development server
python manage.py runserver

# Create new app
python manage.py startapp [app_name]

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Open Python shell
python manage.py shell

# Database shell
python manage.py dbshell

# Collect static files
python manage.py collectstatic
```

## 🎨 Templates

The project uses Django's template system with:
- Template inheritance (base.html)
- Template tags and filters
- Static file inclusion
- Context variable rendering

**Base Template** (`templates/base.html`):
```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    {% include 'navbar.html' %}
    {% block content %}{% endblock %}
</body>
</html>
```

## 📝 Form Handling

Each app includes form classes for:
- Creating/updating models
- User input validation
- CSRF protection
- Error messages

Example:
```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
```

## 🔐 Admin Interface

Access admin at: http://localhost:8000/admin

Configure admin in each app's `admin.py`:
```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date']
    search_fields = ['title', 'content']
    list_filter = ['published_date', 'category']
```

## 🧪 Testing

Create tests for each app:
```bash
python manage.py test blog
python manage.py test courses
python manage.py test products
```

## 🌐 URL Configuration

Main URL routing in `trydjango/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('products/', include('products.urls')),
    path('', include('pages.urls')),
]
```

## 🚀 Extending the Project

### Add New App
```bash
python manage.py startapp [app_name]
```

### Add New Model
1. Define model in `models.py`
2. Create migration: `python manage.py makemigrations`
3. Apply migration: `python manage.py migrate`
4. Register in `admin.py`

### Add New View
1. Create function/class in `views.py`
2. Add URL pattern in `urls.py`
3. Create template in `templates/`

## 📊 Database Models

Each app contains relevant models:
- **Blog**: Post, Category, Comment
- **Courses**: Course, Lesson, Enrollment
- **Products**: Product, Category, Review
- **Pages**: Page

## 🔍 Search & Filter

Implement search and filtering:
- QuerySet filters in views
- Search forms for user input
- Query parameter handling

## 📚 Static Files

Static files location: `static/`
- CSS files
- JavaScript files
- Images
- Other assets

## 🎓 Learning Topics

✅ Django app architecture  
✅ Models and relationships  
✅ Views and routing  
✅ Template rendering  
✅ Form handling  
✅ Admin customization  
✅ URL configuration  
✅ QuerySets and ORM  
✅ Migrations  

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Template not found | Check TEMPLATES setting in settings.py |
| Static files not loading | Run `python manage.py collectstatic` |
| Migration conflicts | Delete migrations and re-create them |
| App not showing in admin | Register model in admin.py |

## 📝 Configuration

Key settings in `trydjango/settings.py`:
- `INSTALLED_APPS`: Add your apps here
- `DATABASES`: Database configuration
- `TEMPLATES`: Template configuration
- `STATIC_URL`: Static files URL

## 🚀 Next Steps

1. Explore each app's models
2. Review views and URL routing
3. Check templates and styling
4. Add new features
5. Test thoroughly
6. Deploy to production

## 🌟 Best Practices

- Keep apps modular and focused
- Use template inheritance
- Follow Django naming conventions
- Write tests for critical functions
- Use QuerySet efficiently
- Secure admin access

---

**Happy Django Development! 🚀**
