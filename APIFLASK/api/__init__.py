from flask import Flask,jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import urllib
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Primera aplicación con Flask'
