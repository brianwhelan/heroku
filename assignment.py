from flask import Flask, jsonify, make_response, request, abort

app = Flask(__name__)
app.debug = True

cal_List = []

@app.route('/myCalendar/<int:cal_id>', methods = ['POST'])
def create_cal(cal_id):
	for c in cal_List:
		if c['ID'] == cal_id: 
			return "Calendar already exists", 409
	newCal = {'ID':cal_id,'Entries':[]}
	cal_List.append(newCal)
	return "Calendar Created", 201

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify( {'error': 'Not found'} ), 404)

@app.route('/myCalendar/<int:cal_id>/Entry/<int:entry_id>',methods = ['POST'])
def create_entry(cal_id,entry_id):
	if not request.json or not 'title' in request.json:
		abort(400)
	thisEntry = {
		'ID': entry_id,
		'title': request.json['title'],
		'description': request.json.get('description', ""),
		'start': request.json.get('start', ""),
		'end': request.json.get('end', ""),
		'location': request.json.get('location', ""),
		'repeat': request.json.get('repeat', "")
	}
	
	for c in cal_List:
		if c['ID'] == cal_id:
			for e in c['Entries']:
				if e == {}:
					c['Entries'].remove({})
					c['Entries'].append(thisEntry)
					return "Success\n", 201
				if e['ID'] == entry_id:
					return "This Entry number already exists for this calendar\n", 409

			c['Entries'].append(thisEntry)
			return "Success\n" , 201

	return "This Calendar ID does not exist\n", 404

@app.route('/myCalendar/<int:cal_id>/Entry/<int:entry_id>',methods = ['DELETE'])
def delete_entry(cal_id,entry_id):
	if not request.json or not 'title' in request.json:
		abort(400)
	
	for c in cal_List:
		if c['ID'] == cal_id:
			for e in c['Entries']:
				if e['ID'] == entry_id:
					e.clear()

					return "Successfully deleted entry\n"


	return "Entry does not exist in this Calendar\n", 404


@app.route('/showCal', methods = ['GET'])
def getCal():
	return jsonify( { 'cal_List': cal_List } ), 201



if __name__ == '__main__':
	app.run(debug = True)
