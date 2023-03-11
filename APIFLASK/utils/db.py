from flask_sqlalchemy import SQLAlchemy
from api import app

DATABASE_CONNECTION = 'mysql://root:Americo27#@127.0.0.1/retail?charset=utf8'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)