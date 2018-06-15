#!flask/bin/python
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Fruit, Eggs',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to work on a good API tutorial',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
        
