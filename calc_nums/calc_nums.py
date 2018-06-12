#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from flask import Flask, request, render_template, abort
from urllib import unquote_plus
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
    Sends a POST request to localhost:5000/api/print with
    a JSON body with a and b.
    """
    a = request.args.get("a")
    b = request.args.get("b")
    return json.dumps("{'a': %s, 'b': %s}" % (a,b))

if __name__ == '__main__':
    app.run(debug=True)

