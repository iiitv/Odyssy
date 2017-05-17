# Odyssy - IIIT Vadodara Website

[![Gitter](https://badges.gitter.im/iiitv/Odyssy.svg)](https://gitter.im/iiitv/Odyssy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

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

#### Migrate Database and Run
```sh
$ cd wsgy/odyssy
$ python manage.py migrate
$ python manage.py runserver
```
