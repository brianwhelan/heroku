import os
import json
from flask import Flask

app = Flask(__name__)

cal_ID = 0

@app.route('/')
def createCal:
	cal_ID = cal_ID + 1
	cal = {'ID':cal_ID}
	entry_ID = 0
	return cal_ID
	

@app.route('/1')
def test():

	return "This is a test page!"
