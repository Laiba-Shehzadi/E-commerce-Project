# 🛍️ MyShop – E-Commerce Web Store

MyShop is a basic full-stack e-commerce web application built with **Python and Django**. It provides a complete shopping workflow from browsing products to placing and viewing orders.

## ✨ Features

- Product listing
- Product details
- User registration and login
- Shopping cart
- Checkout and order processing
- My Orders
- Order details
- Django Admin Panel
- SQLite database
- Responsive UI

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Django
- **Database:** SQLite

## 📁 Project Structure

- Ecommerce-Project/
- │
- ├── accounts/        # User registration and authentication
- ├── store/           # Products and product details
- ├── cart/            # Cart, checkout and orders
- ├── ecommerce/       # Project settings and URLs
- ├── static/          # CSS and static files
- ├── media/           # Product images
- ├── manage.py
- ├── requirements.txt
- └── README.md

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Laiba-Shehzadi/E-commerce-Project.git
````

### 2. Open the Project Folder

```bash
cd E-commerce-Project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Database Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create your admin account.

### 8. Start the Development Server

```bash
python manage.py runserver
```

### 9. Open the Application

Visit:

```text
http://127.0.0.1:8000/
```

### 10. Open Django Admin

Visit:

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser account created in Step 7.

```
### Developer
- Laiba Shehzadi 




