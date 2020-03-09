#!/usr/bin/env python
from flask import (Flask, jsonify, request, abort, render_template, logging)
from flask_cors import CORS
from calculator import Calculator

app = Flask(__name__)
CORS(app)

@app.route('/')
def index_page():
    return "This is a RESTful Calculator App built with Python Flask! - testing my CI/CD Pipeline"

@app.route('/add', methods=['POST'])
def add_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.add(arg1, arg2)
        app.logger.info('{ "operation": "add", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/subtract', methods=['POST'])
def subtract_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.subtract(arg1, arg2)
        app.logger.info('{ "operation": "subtract", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/multiply', methods=['POST'])
def multiply_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.multiply(arg1, arg2)
        app.logger.info('{ "operation": "multiply", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/divide', methods=['POST'])
def divide_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.divide(arg1, arg2)
        app.logger.info('{ "operation": "divide", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)
    except ZeroDivisionError:
        abort(400)

@app.route('/sqrt', methods=['POST'])
def sqrt_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        calculator = Calculator()
        answer = calculator.sqrt(arg1)
        app.logger.info('{ "operation": "sqrt", "arg1": "%s", "arg2": "none", "answer": "%s" }', arg1, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/cbrt', methods=['POST'])
def cbrt_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        calculator = Calculator()        
        answer = calculator.cbrt(arg1)
        app.logger.info('{ "operation": "cbrt", "arg1": "%s", "arg2": "none", "answer": "%s" }', arg1, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/exp', methods=['POST'])
def exponent_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()        
        answer = calculator.exp(arg1, arg2)
        app.logger.info('{ "operation": "exp", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/factorial', methods=['POST'])
def factorial_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        calculator = Calculator()          
        answer = calculator.factorial(arg1)
        app.logger.info('{ "operation": "factorial", "arg1": "%s", "arg2": "none", "answer": "%s" }', arg1, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
