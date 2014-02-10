import os

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
	
	return "Silly Brian"

@app.route('/test')

def add():

	return "This is a test page!"
