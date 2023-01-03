from flask import Flask

app = Flask(__name__)

@app.route("/api")
def status():
	msg = {}
	msg['status'] = "OK"
	msg['sensors'] = {
		'online': 13,
		'offline': 2
	}
	return msg

@app.route("/api/<user_id>")
def user(user_id):
	msg = {}
	msg['id'] = user_id
	msg['name'] = 'Name'
	msg['sensor_info'] = {
		'total': 15,
		'online': 13,
		'offline': 2,
	}
	msg['sensors'] = [
		{
			'id': '87se7fs',
			'name': None,
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': 'My Sensor',
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': 'My Sensor 2',
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': 'My Sensor 3',
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': None,
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': None,
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': None,
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': None,
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': None,
			'online': False
		},
		{
			'id': '8f7sd89',
			'name': None,
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': None,
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': None,
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': 'My Sensor 4',
			'online': False
		},
		{
			'id': '8f7sd89',
			'name': None,
			'online': True
		},
		{
			'id': '8f7sd89',
			'name': None,
			'online': True
		}
	]
	return msg

@app.route("/api/<user_id>/<sensor_id>")
def sensor(user_id, sensor_id):
	msg = {}
	msg['id'] = sensor_id
	msg['name'] = 'Name'
	msg['type'] = 'Type'
	msg['online'] = True
	msg['value'] = 123.456
	return msg