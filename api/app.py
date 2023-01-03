from flask import Flask
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api")
@cross_origin()
def status():
	msg = {}
	msg['status'] = "OK"
	msg['sensors'] = {
		'online': 13,
		'offline': 2
	}
	return msg

@app.route("/api/<user_id>")
@cross_origin()
def user(user_id):
	msg = {}
	msg['id'] = user_id
	msg['name'] = 'Name'
	msg['sensor_info'] = {
		'total': 15,
		'online': 13,
		'offline': 2,
	}
	msg['sensors'] = []
	for i in range(1, random.randrange(10, 30)):
	    msg['sensors'].append({
	        'id': i,
	        'name': 'Name',
	        'online': True
	    })
	return msg

@app.route("/api/<user_id>/<sensor_id>")
@cross_origin()
def sensor(user_id, sensor_id):
	msg = {}
	msg['id'] = sensor_id
	msg['name'] = 'Name'
	msg['type'] = random.choice(['temp', 'humid', 'light', 'winds', 'windd', 'idk'])
	msg['online'] = bool(random.getrandbits(1))
	msg['value'] = 123.456
	return msg
