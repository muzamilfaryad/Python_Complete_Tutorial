# Ecommerce Project

A complete full-stack e-commerce application with Django REST Framework backend and React frontend.

## 📚 Overview

This project demonstrates a modern, scalable e-commerce platform with:
- **Backend**: Django REST API for product management, cart, orders, and user authentication
- **Frontend**: React.js application with responsive UI for shopping experience
- **Integration**: Seamless backend-frontend communication via REST API

## 🎯 Key Features

### Backend
✅ Product management system  
✅ User authentication and authorization  
✅ Shopping cart functionality  
✅ Order processing and tracking  
✅ Inventory management  
✅ Admin dashboard  
✅ API endpoints for all operations  

### Frontend
✅ Product browsing and search  
✅ Shopping cart management  
✅ Checkout process  
✅ User account management  
✅ Order history  
✅ Responsive design  
✅ Real-time cart updates  

## 📂 Project Structure

```
Ecommerce_Project/
├── Backend/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── products/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── store/
│   │   └── ...
│   └── media/
│
└── Frontend/
    └── frontend/
        ├── package.json
        ├── src/
        │   ├── components/
        │   ├── pages/
        │   ├── App.jsx
        │   └── index.jsx
        └── public/
```

## 🚀 Getting Started

### Backend Setup

#### Prerequisites
- Python 3.8+
- Django 3.0+
- Django REST Framework
- SQLite or PostgreSQL

#### Installation

1. Navigate to backend directory:
```bash
cd Backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

If requirements.txt doesn't exist:
```bash
pip install django djangorestframework python-decouple django-cors-headers
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

**Backend URL**: http://localhost:8000

---

### Frontend Setup

#### Prerequisites
- Node.js 14+
- npm or yarn

#### Installation

1. Navigate to frontend directory:
```bash
cd Frontend/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Install required packages (if not already installed):
```bash
npm install react-router-dom axios
```

4. Start development server:
```bash
npm run dev
```

**Frontend URL**: http://localhost:3000 (or as configured)

---

## 🔧 Backend API Endpoints

### Products
```
GET    /api/products/           - List all products
POST   /api/products/           - Create product (admin only)
GET    /api/products/{id}/      - Get product details
PUT    /api/products/{id}/      - Update product (admin only)
DELETE /api/products/{id}/      - Delete product (admin only)
```

### Users
```
POST   /api/users/register/     - Register new user
POST   /api/users/login/        - User login
GET    /api/users/profile/      - Get user profile
PUT    /api/users/profile/      - Update user profile
```

### Cart
```
GET    /api/cart/               - Get cart items
POST   /api/cart/               - Add to cart
PUT    /api/cart/{item_id}/     - Update cart item
DELETE /api/cart/{item_id}/     - Remove from cart
```

### Orders
```
GET    /api/orders/             - List user orders
POST   /api/orders/             - Create new order
GET    /api/orders/{id}/        - Get order details
PUT    /api/orders/{id}/        - Update order status (admin)
```

## 🛠️ Database Models

### Product
- id, name, description, price, stock, category
- created_at, updated_at

### User
- id, username, email, password_hash
- first_name, last_name, profile_pic

### Cart
- id, user, product, quantity
- added_at, updated_at

### Order
- id, user, total_price, status
- shipping_address, created_at, updated_at

### OrderItem
- id, order, product, quantity, price

## 🔐 Authentication

- JWT tokens or session-based authentication
- Protected endpoints require authentication
- Admin-only endpoints require superuser status

## 📝 Environment Configuration

Create a `.env` file in Backend directory:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

## 🚀 Development Workflow

1. **Backend Changes**
   - Modify models → Run migrations
   - Update serializers
   - Create/update views
   - Test with Postman or REST client

2. **Frontend Changes**
   - Update React components
   - Modify styles
   - Update API calls
   - Test in browser

3. **Testing**
   ```bash
   # Backend testing
   python manage.py test
   
   # Frontend testing
   npm test
   ```

## 📦 Deployment

### Backend Deployment (Django)
1. Set DEBUG = False
2. Configure proper ALLOWED_HOSTS
3. Use PostgreSQL instead of SQLite
4. Collect static files: `python manage.py collectstatic`
5. Deploy to: Heroku, AWS, DigitalOcean, etc.

### Frontend Deployment (React)
1. Build production bundle: `npm run build`
2. Deploy to: Vercel, Netlify, AWS S3, etc.
3. Configure API endpoint for production

## 📚 API Documentation

Use Django REST Framework's built-in browsable API:
- http://localhost:8000/api/ (view all endpoints)
- http://localhost:8000/api/products/ (view products endpoint)

## 🔍 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| CORS error | Install django-cors-headers and configure CORS_ALLOWED_ORIGINS |
| 404 Not Found | Check API endpoint paths and URL configuration |
| Port already in use | Use different port: `python manage.py runserver 8001` |
| npm install fails | Delete node_modules and package-lock.json, then reinstall |
| Database error | Run `python manage.py migrate` |

## 🎓 Learning Topics

✅ Django ORM and models  
✅ REST API design  
✅ Serializers and validation  
✅ Authentication and permissions  
✅ React components and hooks  
✅ Frontend routing  
✅ API integration  
✅ State management  
✅ Full-stack application flow  

## 📖 Next Steps

1. Set up database and create models
2. Build API endpoints
3. Create React components
4. Implement authentication
5. Add shopping cart functionality
6. Test all features
7. Deploy to production

## 🤝 Contributing

1. Create a feature branch
2. Make changes
3. Test thoroughly
4. Submit pull request

## 📝 Notes

- Keep backend and frontend running simultaneously during development
- Use Chrome DevTools for frontend debugging
- Use Django admin for backend data management
- Check console logs for errors and debugging

---

**Happy Shopping Experience Development! 🛒**
