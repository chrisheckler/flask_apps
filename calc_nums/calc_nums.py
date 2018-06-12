#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from flask import Flask, request, render_template, abort, jsonify
import json
import re

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Index page describing app
    """
    return (render_template('home.html'), 200, None)


@app.route('/api/print', methods=['GET'])
def print_test():
    """
    Sends a request to localhost:5000/api/print and prints
    variables in json.
    """
    a = request.args.get("a")
    b = request.args.get("b")
    return json.dumps("{'a': %s, 'b': %s}" % (a,b))


@app.route('/api/add', methods=['GET'])
def add_nums():
    """
    Sends a request and returns the sum of the variables.
    """
    a = request.args.get('a',0,type=int)
    b = request.args.get('b',0,type=int)
    return jsonify(a + b) 


@app.route('/api/sub', methods=['GET'])
def sub_nums():
    """
    Sends a request and returns the sum of the variables.
    """
    a = request.args.get('a',0,type=int)
    b = request.args.get('b',0,type=int)
    return jsonify(a - b) 


if __name__ == '__main__':
    app.run(debug=True)

