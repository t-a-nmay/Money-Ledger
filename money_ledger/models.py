from money_ledger import db, login_manager
from money_ledger import bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.types import DECIMAL
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    transactions=db.relationship('Transaction', backref='user', lazy=True)

    @property   
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash=bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email_address}')"

class Transaction(db.Model):
    userid=db.Column(db.Integer(),db.ForeignKey('user.id'))
    transactionid = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.DECIMAL(10,2),nullable=False)
    type = db.Column(db.String(10),nullable=False,unique=False)
    date = db.Column(db.Date(),nullable=False,unique=False)
    description = db.Column(db.String(100), nullable=False, unique=False)
    
   
