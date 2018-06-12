#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from flask import Flask, request
import urllib
import json
import re
 
app = Flask(__name__)

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
    return ("This api performs calculations on a pair of numbers.  " + 
            "These calculations include addition, subtraction, division," +
            "and multiplication.", 200, None)


if __name__=='__main__':
    app.run(debug=True)
