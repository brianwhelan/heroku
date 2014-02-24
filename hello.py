import os

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():

	x = 10	
	
	return x

@app.route('/test')

def add():

	return "This is a test page!"
