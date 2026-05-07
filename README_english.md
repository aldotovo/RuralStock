# RuralStock

A web-based system designed to manage inventory in small-scale rural operations, with a focus on input tracking, stock movement control, and data visualization through a dashboard.

---

## About the Project

RuralStock was developed based on real-world experience in fish farming, where managing inputs such as feed, salt, vaccines, chemical products, and stock levels is essential for daily operations.

The project was expanded to support small rural properties in general, providing a simple and effective solution for inventory management, traceability of inputs, and real-time monitoring of available resources.

Its main goal is to contribute to the digital transformation of rural management processes, helping producers improve decision-making and reduce operational losses.

---

## Purpose

To provide an accessible tool for small farmers and rural businesses to manage inventory efficiently, track stock movements, and visualize data through a dashboard.

---

## Features

- Input category management  
- Product registration  
- Real-time stock control  
- Entry and exit tracking (movements)  
- Automatic stock updates  
- Dashboard with graphical visualization  
- Admin interface for data management  

---

## Target Audience

- Small-scale farmers  
- Fish farmers  
- Rural businesses  
- Agricultural technicians and managers  

---

## Key Highlights

- Built from real-world agricultural experience  
- Focus on improving rural management processes  
- Simple and intuitive design  
- Integration between backend logic and data visualization  

---

## Technologies Used

- Python  
- Django  
- SQLite (default database)  
- HTML / CSS  
- Chart.js (data visualization)  

---

## How to Run the Project

```bash
# Clone the repository
git clone https://github.com/your-username/ruralstock.git

# Navigate to the project folder
cd ruralstock

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver

Once the server is running, you can access:

- Admin panel: http://127.0.0.1:8000/admin  
- Dashboard: http://127.0.0.1:8000/dashboard/


##  Additional Documentation

- [Project Scope](docs/scope.md)
- [Database Modeling](docs/modeling.md)