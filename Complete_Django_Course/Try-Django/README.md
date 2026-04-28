# Try-Django Projects

This is a complete course with projects.

A collection of Django projects demonstrating various aspects of Django development, from REST API creation to full-stack e-commerce applications.

## 🎯 Projects Overview

### 1. **DRF (Django REST Framework)**
REST API development project showcasing Django REST Framework features.

**Features:**
- RESTful API endpoints
- Serializers for data validation
- API views and viewsets
- Request/response handling
- JSON data exchange

**Setup:**
```bash
cd DRF/drf
python manage.py migrate
python manage.py runserver
```

**Access:** http://localhost:8000/api

**Documentation:** See [DRF README](./DRF/README.md)

---

### 2. **Ecommerce_Project**
Complete full-stack e-commerce application with Django backend and React frontend.

**Backend Features:**
- Product management API
- User authentication
- Shopping cart system
- Order processing
- Admin dashboard
- Inventory management

**Frontend Features:**
- Product catalog
- Search and filter
- Shopping cart UI
- Checkout process
- User authentication
- Order history

**Tech Stack:**
- Backend: Django, Django REST Framework
- Frontend: React.js, React Router
- Database: SQLite/PostgreSQL
- Package Management: pip, npm

**Setup Backend:**
```bash
cd Ecommerce_Project/Backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Setup Frontend:**
```bash
cd Ecommerce_Project/Frontend/frontend
npm install
npm run dev
```

**Access:**
- Backend API: http://localhost:8000
- Frontend: http://localhost:3000 (or as configured)

**Documentation:** See [Ecommerce README](./Ecommerce_Project/README.md)

---

### 3. **src**
Traditional Django web application with multiple apps.

**Apps:**
- **blog**: Blog post management and display
- **courses**: Course listing and details
- **pages**: Static and dynamic pages
- **products**: Product catalog

**Features:**
- Template-based rendering
- Form handling
- Database models
- Admin interface
- URL routing
- Static files management

**Setup:**
```bash
cd src
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Access:**
- Home: http://localhost:8000
- Admin: http://localhost:8000/admin

**Documentation:** See [src README](./src/README.md)

---

## 📚 File Structure

```
Try-Django/
├── DRF/
│   ├── drf/
│   │   ├── manage.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── urls.py
│   │   └── drf/
│   │       ├── settings.py
│   │       ├── urls.py
│   │       └── asgi.py
│   │
├── Ecommerce_Project/
│   ├── Backend/
│   │   ├── manage.py
│   │   ├── backend/
│   │   ├── products/
│   │   ├── store/
│   │   └── media/
│   │
│   └── Frontend/
│       └── frontend/
│           ├── package.json
│           ├── src/
│           └── public/
│
├── src/
│   ├── manage.py
│   ├── blog/
│   ├── courses/
│   ├── pages/
│   ├── products/
│   ├── templates/
│   └── trydjango/
│
└── README.md (this file)
```

## 🛠️ Common Setup Steps

### 1. Create Virtual Environment (Python)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. Install Python Dependencies
```bash
pip install django
pip install djangorestframework
pip install python-decouple
```

### 3. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

## 🔧 Available Management Commands

```bash
# View all available commands
python manage.py help

# Create new app
python manage.py startapp [app_name]

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic

# Shell access
python manage.py shell

# Database shell
python manage.py dbshell
```

## 🌐 API Endpoints (DRF & Ecommerce)

The REST API provides endpoints for:
- `/api/products/` - Product listing and creation
- `/api/users/` - User management
- `/api/orders/` - Order management
- `/api/cart/` - Shopping cart operations

## 📖 Learning Topics

✅ Django models and ORM  
✅ Database migrations  
✅ Views and routing  
✅ Template system  
✅ Form handling  
✅ REST API development  
✅ Serializers and validators  
✅ Authentication and permissions  
✅ Full-stack integration  
✅ Frontend-backend communication  

## 🚀 Deployment Considerations

- Use PostgreSQL instead of SQLite for production
- Configure environment variables
- Set DEBUG = False in production
- Use proper ALLOWED_HOSTS
- Enable CORS for cross-origin requests
- Implement proper error handling
- Use HTTPS in production

## 📝 Notes

- Each project has its own database (db.sqlite3)
- Virtual environments are recommended
- Install dependencies before running projects
- Check individual project READMEs for specific configurations
- Frontend requires Node.js and npm

## 🐛 Troubleshooting

**ModuleNotFoundError**: Ensure virtual environment is activated  
**Database locked**: Delete db.sqlite3 and run migrations again  
**Port in use**: Run on different port: `python manage.py runserver 8001`  
**CORS issues**: Check CORS settings in backend Django settings  

## 🎓 Project READMEs

For detailed information about each project, refer to:
- [DRF Project README](./DRF/README.md)
- [Ecommerce Project README](./Ecommerce_Project/README.md)
- [Django Application README](./src/README.md)

---

**Continue Learning & Building! 🎓**
