#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:str>')
def print_string(str):
    print(str)
    return str

@app.route('/count/<int:num>')
def count(num):
    return '\n'.join([str(i) for i in range(num)]) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return '<p>Can not divide by 0</p>'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return '<p>Invalid operation</p>'
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
