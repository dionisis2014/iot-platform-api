# ORM
Documentation for the ORM used

## ORM used
The ORM used is the [SQLAlchemy](https://www.sqlalchemy.org/) python library. It was chosen for the easy integration of a databse with a python class. All CRUD operations are done with simple class member operators and a transaction commit at the end to finalize the operation in an atomic way.

## Connector
The connector used is [PyMySQL](https://github.com/PyMySQL/PyMySQL/), a pure python implmentation of a MySQL client library. This is used to interface the ORM with the [database](DB.md) at a low level. It was chosen for its compatibility and low dependencies (doesn't need mariadb installed on system).

## Engine
The engine is the SQL statement generator used by [SQLAlchemy](https://www.sqlalchemy.org/). It is used to convert the function calls to SQL statements to be sent to the database via the [connector](#Connector). The engine takes a URI as an argument to configure the various parts of the ORM. In this case the URI specified is `mariadb+pymysql://api:password@api.mewhenthe.xyz/iot_platform`. It can be broken down to:
- `mariadb`: Hint for the engine of the type of database used
- `pymysql`: The connector to be used
- `api:password`: The user and password to connect under
- `api.mewhenthe.xyz`: The IP of the database system
- `iot_platform`: The database to be used