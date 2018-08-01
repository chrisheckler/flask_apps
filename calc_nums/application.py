#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from flask import Flask, request, render_template, jsonify
import json


applicationlication = Flask(__name__)


@application.route('/', methods=['GET'])
def index():
    """
    Index page describing application
    """
    return (render_template('home.html'), 200, None)


@application.route('/api/print', methods=['GET'])
def print_test():
    """
    Sends a request to localhost:5000/api/print and prints
    variables in json.
    """
    a = request.args.get("a")
    b = request.args.get("b")
    return json.dumps("{'a': %s, 'b': %s}" % (a, b))


@application.route('/api/add', methods=['GET'])
def add_nums():
    """
    Sends a request and returns the sum of the variables.
    """
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(a + b)


@application.route('/api/sub', methods=['GET'])
def sub_nums():
    """
    Sends a request and returns the subtraction of the variables.
    """
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(a - b)


@application.route('/api/mult', methods=['GET'])
def mult_nums():
    """
    Sends a request and returns the product of the variables.
    """
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(a * b)


@application.route('/api/div', methods=['GET'])
def div_nums():
    """
    Sends a request and returns the divided nums.
    """
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)

    try:
        return jsonify(a / b)

    except ZeroDivisionError:
        error = 'Cannot divide by 0!'
        return error


if __name__ == '__main__':
    application.run(debug=True)
