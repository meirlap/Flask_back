# Flask Backend

This project is the backend of a web application built with Flask. It provides API routes to fetch and manage data such as customers, employees, products, and orders from a local SQL Server database.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Routes](#api-routes)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd pythonProject
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Configure the database connection:
   Update the database connection settings in `config.py` if necessary. Make sure the SQL Server database is running and accessible.

## Usage

To start the Flask server, run:
```bash
flask run
The application will be available at http://localhost:5000.


Project Structure
The project structure is as follows:

arduino
Copy code
pythonProject/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── ...
├── migrations/
│   └── ...
├── instance/
│   └── ...
├── .gitignore
├── config.py
├── run.py
├── requirements.txt
└── README.md
API Routes
The backend provides the following API routes:

GET /api/customers: Fetch all customers
GET /api/employees: Fetch all employees
GET /api/products: Fetch all products
GET /api/orders: Fetch all orders
GET /api/orders/customer/<customer_id>: Fetch orders for a specific customer
POST /api/orders: Create a new order
