#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

# Home page for this app
@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/add')
def add_num():
    return render_template('add_num.html')

@app.route('/sub')
def add_num():
    return render_template('sub_num.html')

@app.route('/mult')
def add_num():
    return render_template('mult_num.html')

@app.route('/div')
def add_num():
    return render_template('div_num.html')

if __name__=='__main__':
    app.run(debug=True)
