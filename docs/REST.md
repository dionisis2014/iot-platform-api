# REST server
Documentation for the REST server used

## Server used
The REST server used is the [Flask](https://flask.palletsprojects.com/) python library. It was chosen for its easy use at defining endpoints and their attributes.

## Entrypoints
Below is a list of all endpoints that are implemented:
URL | Documentation
--- | ---
`/api/users` | [API_USERS](rest/API_USERS.md)
`/api/users/<user_name>` | [API_USERS_USERNAME](rest/API_USERS_USERNAME.md)
`api/<user_name>/<sensor_id>` | [API_USERNAME_SENSORID](rest/API_USERNAME_SENSORID.md)
