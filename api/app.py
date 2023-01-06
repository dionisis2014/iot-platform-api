from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session, relationship
from sqlalchemy import Column, Integer, Boolean, Float, String, select, ForeignKey

URI_DB_REMOTE = 'mariadb+pymysql://api:password@api.mewhenthe.xyz/iot_platform'
URI_DB_LOCAL = 'sqlite:///sqlite.db'

app = Flask(__name__)
engine = create_engine(URI_DB_REMOTE, echo=True, future=True)

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(32), nullable=False)

	def __repr__(self):
		return f"User(id={self.id!r}, name={self.name!r})"

	def toDict(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Sensor(Base):
	__tablename__ = 'sensors'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(32), default=None)
	online = Column(Boolean, default=False, nullable=False)
	type = Column(String(32), nullable=False)
	value = Column(Float(precision=16), default=None)
	user_id = Column(ForeignKey("users.id", ondelete="cascade"), nullable=False)

	def __repr__(self):
		return f"Sensor(id={self.id!r}, name={self.name!r}, online={self.online!r}, type={self.type!r}, value={self.value!r}, user={self.user_id!r})"
	
	def toDict(self):
		return {
			'id': self.id,
			'name': self.name,
			'online': self.online,
			'type': self.type,
			'value': self.value,
			'user_id': self.user_id
		}

Base.metadata.create_all(engine, checkfirst=True)

def getUserId(session, id):
	statement = select(User).where(User.id.__eq__(id))
	return session.scalar(statement)

def getUserName(session, name):
	statement = select(User).where(User.name.__eq__(name))
	return session.scalar(statement)

def getSensor(session, id):
	statement = select(Sensor).where(Sensor.id.__eq__(id))
	return session.scalar(statement)

@app.route("/api/users", methods=['GET', 'POST'])
def users():
	with Session(engine) as session:
		if request.method == 'GET':
			statement = select(User)
			users = session.scalars(statement)
			users_list = []
			for user in users:
				users_list.append(user.name)
			return {"users": users_list}
		elif request.method == 'POST':
			data = request.get_json()
			if 'name' in data:
				if not isinstance(data['name'], str):
					return {"error": "\'name\' is not a string"}
				l = Sensor.name.property.columns[0].type.length
				if len(data['name']) > l:
					return {"error": f"\'name\' is over {l} characters"}
				user = User(name=data['name'])
				session.add(user)
				try:
					session.commit()
					return {"error": None}
				except Exception as e:
					session.rollback()
					session.flush()
					return {"error": "failed to add new user"}
			else:
				return {"error": "no \'name\' provided"}
		else:
			return {"error": "server error"}

@app.route("/api/users/<user_name>", methods=['GET', 'POST'])
def user(user_name):
	with Session(engine) as session:
		user = getUserName(session, user_name)
		if user is None:
			return {"error": "user doesn't exist"}

		if request.method == 'GET':
			data = user.toDict()
			data['sensors'] = []
			statement = select(Sensor).where(Sensor.user_id.__eq__(user.id))
			sensors = session.scalars(statement)
			for sensor in sensors:
				data['sensors'].append(sensor.id)
			return data
		elif request.method == 'POST':
			sensor = Sensor(user_id=user.id)
			data = request.get_json()
			if 'name' in data:
				if not isinstance(data['name'], str):
					return {"error": "\'name\' is not a string"}
				l = Sensor.name.property.columns[0].type.length
				if len(data['name']) > l:
					return {"error": f"\'name\' is over {l} characters"}
				sensor.name = data['name']
			if 'online' in data:
				if not isinstance(data['online'], bool):
					return {"error": "\'online\' is not a boolean"}
				sensor.online = data['online']
			if 'type' in data:
				if not isinstance(data['type'], str):
					return {"error": "\'type\' is not a string"}
				l = Sensor.name.property.columns[0].type.length
				if len(data['type']) > l:
					return {"error": f"\'type\' is over {l} characters"}
				sensor.type = data['type']
			else:
				return {"error": "no \'type\' provided"}
			session.add(sensor)
			try:
				session.commit()
				return {"error": None}
			except Exception as e:
				session.rollback()
				session.flush()
				return {"error": "failed to add new sensor"}
		else:
			return {"error": "server error"}

@app.route("/api/<user_name>/<int:sensor_id>", methods=['GET', 'DELETE', 'PATCH'])
def sensor(user_name, sensor_id):
	with Session(engine) as session:
		user = getUserName(session, user_name)
		sensor = getSensor(session, sensor_id)
		if user is None:
			return {"error": "user doesn't exist"}
		if sensor is None:
			return {"error": "sensor not found"}
		if sensor.user_id != user.id:
			return {"error": "sensor not found for user"}
		if request.method == 'GET':
			return sensor.toDict()
		elif request.method == 'DELETE':
			session.delete(sensor)
			try:
				session.commit()
				return {"error": None}
			except Exception as e:
				session.rollback()
				session.flush()
				return {"error": "failed to delete sensor"}
		elif request.method == 'PATCH':
			data = request.get_json()
			if 'name' in data:
				if not isinstance(data['name'], str):
					return {"error": "\'name\' is not a string"}
				l = Sensor.name.property.columns[0].type.length
				if len(data['name']) > l:
					return {"error": f"\'name\' is over {l} characters"}
				sensor.name = data['name']
			if 'online' in data:
				if not isinstance(data['online'], bool):
					return {"error": "\'online\' is not a boolean"}
				sensor.online = data['online']
			if 'type' in data:
				if not isinstance(data['type'], str):
					return {"error": "\'type\' is not a string"}
				l = Sensor.name.property.columns[0].type.length
				if len(data['type']) > l:
					return {"error": f"\'type\' is over {l} characters"}
				sensor.type = data['type']
			try:
				session.commit()
				return {"error": None}
			except Exception as e:
				session.rollback()
				session.flush()
				return {"error": "failed to edit sensor"}
		else:
			return {"error": "server error"}
