from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from money_ledger.models import User
from datetime import datetime

class RegisterForm(FlaskForm):
    
    def validate_username(self, username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try using a differnt username')
    
    def validate_email_address(self, email_address_to_check):
        email_address=User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email already exists! Please try using a differnt email address')
    
    username = StringField(label='Username : ', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address : ', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password : ', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm Password : ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
    
class LoginForm(FlaskForm):
    username = StringField(label='Username : ', validators=[DataRequired()])
    password = PasswordField(label='Password : ', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
    

class TransactionForm(FlaskForm): 
    def validate_date(self, field):
        try:
            # Convert the date from DD-MM-YYYY to YYYY-MM-DD format
            field.data = datetime.strptime(field.data, '%d-%m-%Y').date()
        except ValueError:
            raise ValidationError('Invalid date format. Please use DD-MM-YYYY.')
    
    def validate_type(self, field):
        if field.data not in ['Income', 'Expense', 'Transfer']:
            raise ValidationError('Please select a valid type (Income, Expense, or Transfer)')
    
    amount = FloatField(label='Amount : ', validators=[DataRequired()])
    description = StringField(label='Description : ')
    date = StringField(label='Date (DD-MM-YYYY) : ', validators=[DataRequired()])
    type = StringField(label='Income/Expense/Transfer', validators=[DataRequired()])
    submit = SubmitField(label='Add Transaction')