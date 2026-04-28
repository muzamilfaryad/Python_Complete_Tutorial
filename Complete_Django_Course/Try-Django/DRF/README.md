# Django REST Framework (DRF) Project

A Django REST Framework project demonstrating API development with Django.

## 📚 Overview

This project showcases how to build RESTful APIs using Django REST Framework. It includes proper serialization, routing, and request/response handling.

## 🎯 Features

✅ RESTful API endpoints  
✅ Serializers for data validation  
✅ JSON request/response handling  
✅ API views and viewsets  
✅ URL routing for API  
✅ Database models  
✅ Admin integration  

## 📂 Project Structure

```
drf/
├── manage.py
├── db.sqlite3
├── api/
│   ├── __init__.py
│   └── urls.py
│
└── drf/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Django 3.0+
- Django REST Framework

### Installation

1. Navigate to project directory:
```bash
cd drf
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django djangorestframework
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser (optional):
```bash
python manage.py createsuperuser
```

6. Start development server:
```bash
python manage.py runserver
```

## 🔧 API Endpoints

Access the API at: `http://localhost:8000/api/`

Common endpoints structure:
```
GET    /api/resource/        - List all resources
POST   /api/resource/        - Create new resource
GET    /api/resource/{id}/   - Retrieve specific resource
PUT    /api/resource/{id}/   - Update resource
DELETE /api/resource/{id}/   - Delete resource
```

## 📖 Key Concepts

### Serializers
Serializers define how to convert Python objects to JSON and validate incoming data.

### Views
- APIView: Class-based views for custom API logic
- ViewSets: Automated CRUD views
- Generic Views: Pre-built views for common operations

### Routing
URL patterns map HTTP requests to view functions/classes.

## 🛠️ Management Commands

```bash
# Run development server
python manage.py runserver

# Create new app
python manage.py startapp [app_name]

# Database operations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Database shell
python manage.py dbshell

# Python shell
python manage.py shell
```

## 📝 Configuration

Key settings in `drf/settings.py`:
- `INSTALLED_APPS`: Add 'rest_framework' to use DRF
- `REST_FRAMEWORK`: Configure DRF behavior
- `DATABASES`: Database configuration (SQLite by default)

## 🔐 Authentication & Permissions

DRF provides:
- Token-based authentication
- Session-based authentication
- JWT authentication (requires additional package)
- Permission classes for access control

## 📊 Testing

Create tests using Django's testing framework:
```bash
python manage.py test
```

## 🌐 CORS Configuration

For cross-origin requests, install and configure:
```bash
pip install django-cors-headers
```

## 🚀 Next Steps

1. Create API apps and models
2. Build serializers
3. Write views/viewsets
4. Configure URL routing
5. Test API endpoints
6. Add authentication
7. Deploy to production

## 📝 Notes

- Database is SQLite (db.sqlite3) - suitable for development
- For production, use PostgreSQL or MySQL
- Never commit sensitive data or database files
- Use environment variables for configuration

## 🐛 Troubleshooting

**ModuleNotFoundError**: Ensure virtual environment is activated and packages installed  
**Port in use**: `python manage.py runserver 8001`  
**Database errors**: Run `python manage.py migrate` again  

---

**Happy API Building! 🚀**
