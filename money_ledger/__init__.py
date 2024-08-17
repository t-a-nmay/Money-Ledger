import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.engine.url import URL
from flask_login import LoginManager

app=Flask(__name__, static_folder='static')

your_password = "myyySQL12345server" 
uri = URL('mysql', username='root', password=your_password, host='localhost',port=3306, query=None, database='money_ledger')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql+mysqlconnector://root:myyySQL12345server@localhost/money_ledger')
app.config['SECRET_KEY'] = 'aebf23f2d7dca2894e7ddfc813fdd1a4'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from money_ledger import routes
app.register_blueprint(routes.blueprint)
