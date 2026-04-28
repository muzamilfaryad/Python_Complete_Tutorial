# Complete Django Course

This is a complete course with projects.

Welcome to the Complete Django Course project! This directory contains multiple Django projects that demonstrate progressive learning of the Django framework.

## 📚 Projects Overview

### 1. **Try-Django**
A collection of Django projects demonstrating various features:

#### **DRF (Django REST Framework)**
- RESTful API implementation using Django REST Framework
- API endpoints and serializers
- Request/response handling

#### **Ecommerce_Project**
A complete full-stack e-commerce application:
- **Backend**: Django REST API with product management, cart, and order systems
- **Frontend**: React.js application for user interface
- Database models for products, users, and orders
- Integrated payment processing capabilities

### 2. **src**
A traditional Django web application featuring:
- Multiple Django apps: blog, courses, pages, products
- HTML templates with template inheritance
- Form handling and validation
- Database models and migrations
- Admin interface configuration

## 🎯 Key Features

✅ REST API development with DRF  
✅ Full-stack application development  
✅ Database design and migrations  
✅ Admin panel configuration  
✅ Template rendering and static files  
✅ Form handling and validation  

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Django 3.0+
- Django REST Framework
- Node.js (for Ecommerce frontend)
- Virtual environment

### Installation

1. Navigate to the project directory
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
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

## 📂 Project Structure

```
Complete_Django_Course/
├── Try-Django/
│   ├── DRF/
│   │   └── drf/
│   │       ├── manage.py
│   │       ├── db.sqlite3
│   │       ├── api/
│   │       └── drf/
│   │
│   ├── Ecommerce_Project/
│   │   ├── Backend/ (Django REST API)
│   │   └── Frontend/ (React.js)
│   │
│   └── src/
│       ├── manage.py
│       ├── blog/
│       ├── courses/
│       ├── pages/
│       ├── products/
│       ├── templates/
│       └── trydjango/
│
└── README.md (this file)
```

## 🔧 Available Commands

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Create Django app
python manage.py startapp [app_name]

# Access admin panel
# Navigate to: http://localhost:8000/admin

# Make migrations
python manage.py makemigrations
```

## 📖 Learning Topics Covered

- Django ORM and models
- Database migrations
- Admin interface
- Views and URL routing
- Template system
- Form handling
- Django REST Framework serializers
- API endpoints (CRUD operations)
- Authentication and permissions
- Full-stack integration

## 🌐 Ecommerce Project Details

### Backend Structure
- Product management system
- User authentication
- Shopping cart functionality
- Order processing
- Admin dashboard

### Frontend Structure
- Product listing and search
- Shopping cart interface
- Checkout flow
- User account management

## 🐛 Troubleshooting

**Port already in use**: Change port with `python manage.py runserver 8001`  
**Database errors**: Run `python manage.py migrate` again  
**Import errors**: Ensure virtual environment is activated  

## 📝 Notes

- Each sub-project can be run independently
- Make sure to activate the virtual environment before running commands
- Database is SQLite by default (db.sqlite3)
- For production, configure proper database (PostgreSQL recommended)

## 🎓 Next Steps

1. Explore DRF project for API concepts
2. Study the src project for traditional Django
3. Build the Ecommerce application end-to-end
4. Customize and extend each project with new features

---

**Happy Coding! 🚀**
