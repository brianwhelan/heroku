from flask import Flask, jsonify, make_response, request, abort

app = Flask(__name__)
app.debug = True

cal_List = []

@app.route('/myCalendar/<int:cal_id>', methods = ['POST'])
def create_cal(cal_id):
	newCal = {'ID':cal_id,'Entries':[]}
	cal_List.append(newCal)
	return "New Calendar Created"

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify( {'error': 'Not found'} ), 404)

@app.route('/myCalendar/<int:cal_id>/Entry/<int:entry_ID>',methods = ['POST'])
def create_entry(cal_id,entry_ID):
	if not request.json or not 'title' in request.json:
		abort(400)
	thisEntry = {
		'ID': entry_ID,
		'title': request.json['title'],
		'description': request.json.get('description', ""),
		'start': request.json.get('start', ""),
		'end': request.json.get('end', ""),
		'location': request.json.get('location', ""),
		'repeat': request.json.get('repeat', "")
	}
	
	for c in cal_List:
		if c['ID'] == cal_id:
			c['Entries'].append(thisEntry)
			return "Success" , 201

	return "Failure", 404


@app.route('/showCal', methods = ['GET'])
def getCal():
	return jsonify( { 'cal_List': cal_List } ), 201



if __name__ == '__main__':
	app.run(debug = True)
