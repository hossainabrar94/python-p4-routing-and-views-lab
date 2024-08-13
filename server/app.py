#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:integer>')
def count(integer):
    count = f''
    for num in range(integer):
        count += f'{num}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,num2, operation):
    if operation == '+':
        return str(num1+num2)
    elif operation =='-':
        return str(num1-num2)
    elif operation == '*':
        return str(num1*num2)
    elif operation =='div':
        return str(num1/num2)
    elif operation == '%':
        return str(num1 % num2)

    return 'Operation not recognized. Please use one of the following: + - * div %'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
