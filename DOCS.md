# API Server Documentation

## General overview
The API server consists of three main parts. The [Database](#Database), the [ORM](#ORM) and the [REST server](#REST-server).

### Database
A relational database ([MariaDB](https://mariadb.org/)) is used to hold the data for the users and the sensors. The database is accessed by a dedicated user with a password known only by the [ORM](#ORM).

See [DB.md](docs/DB.md) for more information.

### ORM
For this project, the [SQLAlchemy](https://www.sqlalchemy.org/) library is used as the ORM to connect the buiness logic with the The [Database](#Database). It is responsible for creating doing all CRUD operations on the `User` and `Sensor` classes defined in the [source code](api/app.py).

See [ORM.md](docs/ORM.md) for more information.

### REST server
For this project, the [Flask](https://flask.palletsprojects.com/) library is used as the REST WSGI server to connect the buiness logic with the frontend application.

See [REST.md](docs/REST.md) for more information.
