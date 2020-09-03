#!/usr/bin/python3
""" script that starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """ List all the states """
    all_states = list(storage.all(State).values())
    return (render_template('7-states_list.html', all_states=all_states))


@app.teardown_appcontext
def teardown(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)    
