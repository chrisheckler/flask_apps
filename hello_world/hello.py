#!/usr/bin/env/ python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)
