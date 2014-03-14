import os

from flask import Flask

app = Flask(__name__)


@app.route('/')

def hello():
	
	return "Hello Again"
	

@app.route('/test')

def test():

	return "This is a test page!"
