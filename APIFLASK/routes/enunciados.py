from flask import Flask,jsonify, request
from api import app
from queries.enunciado1 import *
from queries.enunciado2 import *
from queries.enunciado3 import *
from queries.enunciado4 import *
from utils.db import db



# Enunciado1

@app.route('/api/v1/enunciado1', methods = ['GET'])
def enunciado1():
    response = get_enunciado1()
    return jsonify(response)

@app.route('/api/v1/enunciado2', methods = ['GET'])
def enunciado2():
    response = get_enunciado2()
    return jsonify(response)

@app.route('/api/v1/enunciado3', methods = ['GET'])
def enunciado3():
    response = get_enunciado3()
    return jsonify(response)

@app.route('/api/v1/enunciado4', methods = ['GET'])
def enunciado4():
    response = get_enunciado4()
    return jsonify(response)