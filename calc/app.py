from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def add_route():
    a = request.args['a']
    b = request.args['b']
    answer = add(int(a),int(b))
    return str(answer)

@app.route('/sub')
def sub_route():
    a = request.args["a"]
    b = request.args["b"]
    answer = sub(int(a), int(b))
    return str(answer)

@app.route('/mult')
def mult_route():
    a = request.args["a"]
    b = request.args["b"]
    answer = mult(int(a), int(b))
    return str(answer)

@app.route('/div')
def div_route():
    a = request.args["a"]
    b = request.args["b"]
    answer = div(int(a), int(b))
    return str(answer)

@app.route('/math/<operator>')
def math(operator):
    a = int(request.args["a"])
    b = int(request.args["b"])
    operations = {'add': add(a,b), 'sub': sub(a,b), 'mult': mult(a,b), 'div': div(a,b)}
    return str(operations[operator])
