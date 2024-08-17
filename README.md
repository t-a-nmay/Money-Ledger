
# Money Ledger

**Money Ledger**

Money Ledger is a Flask-based web application designed to help users manage their personal finances. It allows users to track their income, expenses, and transfers, generate detailed reports, and visualize their financial data through charts and graphs.



**Installation**

**Clone the repository**:

git clone https://github.com/your-username/money-ledger.git

**Install the required packages**:
pip install -r requirements.txt
**Create a database**: 
flask db init and flask db migrate and flask db upgrade
**Run the application******:
flask run

**Usage**
Register for an account:
/register

Log in to your account: /login

Add transactions: /add_transaction

View transactions: /transactions

Generate transaction report: /transactions/report

Update transactions: /transactions/<int:transaction_id>/update

Delete transactions: /transactions/<int:transaction_id>/delete

**Project Structure**
app/: Contains the application modules and code.
routes.py: Defines the routes and application logic.
models.py: Defines the database models (User, Transaction, etc.).
forms.py: Defines the forms used in the application.
templates/: Contains HTML templates.
static/: Contains static files like CSS and JavaScript.
migrations/: Handles database migrations.
config.py: Configuration settings for the application.
requirements.txt: Lists all Python dependencies.

**Technologies Used**
Flask web framework
SQLAlchemy ORM
WTForms for form handling
Matplotlib for data visualization
Flask-Login for user authentication
Flask-SQLAlchemy for database integration

**Contributing**
Contributions are welcome! If you'd like to contribute to the project, please fork the repository and submit a pull request.

**Author**
Tanmay

## Features

**User Authentication**:
Secure user registration and login.

**Transaction Management**:
Add, update, and delete income, expense, and transfer transactions.

**Date Format Handling**:
Dates are handled in DD-MM-YYYY format.

**Financial Reports**:
Generate detailed reports of transactions with pie charts for visual representation.

**Responsive Design**:
User-friendly interface with Bootstrap for a responsive and modern design.

**Data Visualization**:
Visualize income, expenses, and transfers through pie charts.

**Flask-WTF Forms**: 
Seamlessly handle form submissions with validation.Getting Started

## Installation

**Installation**
**Prerequisites**
    Python 3.8 or higher
    
    Flask 2.0 or higher
    
    Flask-SQLAlchemy 2.5 or higher
    
    Flask-Login 0.5 or higher
    
    WTForms 2.3 or higher
    
    Matplotlib 3.4 or higher
    
    Installation Steps

**Clone the repository:**
```bash
    git clone https://github.com/t-a-nmay/Money-Ledger.git
```
 
**Create a virtual environment**:
```bash
    python -m venv venv (on Windows) or python3 -m venv venv (on macOS/Linux)
```
    

**Activate the virtual environment**:
```bash
    venv\Scripts\activate (on Windows) or source venv/bin/activate (on macOS/Linux)
```

**Install the required packages**: 
```bash
    pip install -r requirements.txt
```

**Create a database**:
```bash
    flask db init and flask db migrate and flask db upgrade
``` 

**Run the application**: 
```bash
    flask run
``` 



## Usage/

Register for an account: 
/register

Log in to your account: 
/login

Add transactions: /add_transaction

View transactions: /transactions

Generate transaction report: /transactions/report

Update transactions: /transactions/<int:transaction_id>/update

Delete transactions: /transactions/<int:transaction_id>/delete



## Technologies Used

*Flask web framework

*SQLAlchemy ORM

*WTForms for form handling

*Matplotlib for data visualization

*Flask-Login for user authentication

*Flask-SQLAlchemy for database integration

