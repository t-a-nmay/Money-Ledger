from money_ledger import app
from flask import Flask, render_template,request, redirect, url_for, session, flash
from money_ledger.models import Transaction, User
from money_ledger.forms import RegisterForm, LoginForm, TransactionForm
from money_ledger import db
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from wtforms.widgets import DateInput
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
import matplotlib.pyplot as plt
import io
import base64

blueprint = Blueprint('routes', __name__)


# app.config.from_object(Config)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/transactions')
@login_required
def transactions_page():
    transactions=Transaction.query.filter_by(userid=current_user.id).all()
    income_transactions = Transaction.query.filter_by(type='Income', userid=current_user.id).all()
    expense_transactions = Transaction.query.filter_by(type='Expense', userid=current_user.id).all()
    transfer_transactions = Transaction.query.filter_by(type='Transfer', userid=current_user.id).all()
    return render_template('transactions.html', transactions = transactions, income_transactions=income_transactions, expense_transactions=expense_transactions, transfer_transactions=transfer_transactions)

@app.route('/transactions/report', methods=['GET'])
@login_required
def generate_report():
    transactions = Transaction.query.filter_by(userid=current_user.id).all()
    income_transactions = [t for t in transactions if t.type == 'Income']
    expense_transactions = [t for t in transactions if t.type == 'Expense']
    transfer_transactions = [t for t in transactions if t.type == 'Transfer']

    labels = ['Income', 'Expense', 'Transfer']
    sizes = [sum(t.amount for t in income_transactions), sum(t.amount for t in expense_transactions), sum(t.amount for t in transfer_transactions)]
    print(sizes)
    explode = (0.1,0,0)
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    ax.axis('equal')

    img = io.BytesIO()
    fig.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('transactions.html', plot_url=plot_url, transactions=transactions, income_transactions=income_transactions, expense_transactions=expense_transactions, transfer_transactions=transfer_transactions)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('login_page'))
    
    if form.errors !={}:
        for error_msg in form.errors.values():
            flash(f'There was an error while creating an account: {error_msg}',category='danger')
            
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and attempted_user.check_password(attempted_password = form.password.data):
            login_user(attempted_user)
            flash(f'Login Successfull! You are logged in as : {attempted_user.username}', category='success')
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect username or password! PLease try again', category='danger')
            
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out ", category='info')
    return redirect(url_for('home_page'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

    
@app.route('/add_transaction', methods = ['GET', 'POST'])
@login_required
def add_transaction():
    form=TransactionForm()
    if form.validate_on_submit():
        try:
            transaction_to_add = Transaction(amount = form.amount.data, description=form.description.data, date = form.date.data, type=form.type.data)
            transaction_to_add.userid=current_user.id
            db.session.add(transaction_to_add)
            db.session.commit()
            flash('Transaction added successfully!', category="success")
            return redirect(url_for('transactions_page'))
        except Exception as e:
            db.session.rollback()
            flash(f'An Error occurred : {str(e)}', category="error")
    
    return render_template('add_transaction.html',form=form, DateInput=DateInput)

@app.route('/transactions/<int:transaction_id>/update', methods=['GET', 'POST'])
@login_required
def update_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    form = TransactionForm()
    if form.validate_on_submit():
        transaction.date = form.date.data
        transaction.amount = form.amount.data
        transaction.description = form.description.data 
        transaction.type = form.type.data
        db.session.commit()
        flash('Transaction updated successfully!', category="success")
        return redirect(url_for('transactions_page'))
    elif request.method == 'GET':
        form.amount.data = transaction.amount
        form.description.data = transaction.description
        form.date.data = transaction.date.strftime('%d-%m-%Y')
        form.type.data = transaction.type
    else:
        print(form.errors)
    return render_template('update_transaction.html', form=form, DateInput=DateInput)

@app.route('/transactions/<int:transaction_id>/delete', methods=['POST'])
@login_required
def delete_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    flash('Transaction deleted successfully!', category="success")
    return redirect(url_for('transactions_page'))


