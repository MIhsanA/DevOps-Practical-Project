from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import getenv


app = Flask(__name__)
bcrypt = Bcrypt(app)

#getenv('MYSQL_USER')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql:3306/project-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456789++-'
db = SQLAlchemy(app)


from application import routes

