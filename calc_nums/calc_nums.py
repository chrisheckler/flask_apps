#!/usr/bin/env python
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from flask import Flask, request, render_template
from urllib.parse import unquote_plus
import json
import re

app = Flask(__name__, template_folder='templates')


def parse_request(req):
    # Parses requests body into dictionary
    payload = req.get_data()
    payload = unquote_plus(payload)
    payload = re.sub('payload=', '', payload)
    payload = json.loads(payload)

    return payload


@app.route('/', methods=['GET'])
def index():
    """
    Index page describing app
    """
    return (render_template('home.html'), 200, None)


if __name__ == '__main__':
    app.run(debug=True)
