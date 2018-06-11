#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from flask import Flask, request
from urllib import unquote_plus
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




if __name__=='__main__':
    app.run(debug=True)
