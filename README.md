# Odyssy - IIIT Vadodara Website

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2ee2f1779b2f4cacaf8ff1d7b278e10c)](https://www.codacy.com/app/singhpratyush/Odyssy?utm_source=github.com&utm_medium=referral&utm_content=iiitv/Odyssy&utm_campaign=badger)
[![Gitter](https://badges.gitter.im/iiitv/Odyssy.svg)](https://gitter.im/iiitv/Odyssy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Build Status](https://travis-ci.org/iiitv/Odyssy.svg?branch=master)](https://travis-ci.org/iiitv/Odyssy.svg?branch=master)

### Running Locally

#### Set up Database

* Install PostgreSQL (`>=9.2`)
* Log in to `postgres` user
    ```sh
    $ sudo su - postgres
    ```
* Open psql shell
    ```sh
    $ psql
    ```
* Create database, user and grant permission
    ```sql
    create database odyssy;
    create user odyssy with password 'odyssy';
    grant all on database odyssy to odyssy;
    ```
* Exit to root console

#### Clone project
```sh
$ git clone git@github.com:iiitv/Odyssy.git
```

#### Install requirements
```sh
$ cd Odyssy
$ sudo -H pip install -r requirements.txt
```

#### Migrate Database
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

#### Run
```sh
$ ./start.sh
```

### Stop
```sh
$ ./stop.sh
```
