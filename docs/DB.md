# Database
Documentation for the database used

## Database used
The database used is [MariaDB](https://mariadb.org/) on an [Arch Linux](https://archlinuxarm.org/) virtual machine. The database was chosen as the most compatible relational database with the [ORM](ORM.md) used.

## Network
The database is only accessible from the IP address of the [ORM](ORM.md) at the default port (TCP 3306).

## User
The user `api` has been setup to have access only to the database used by the platform, protected by a password only known to the [ORM](ORM.md).

## Database tables
- [Users](db/USERS.md)
- [Sensors](db/SENSORS.md)