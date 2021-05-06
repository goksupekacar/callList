# Information Measurement Project

![Scheme](static/images/logo.jpeg)


## Quick Start

1. Make sure that Python 3.8 (or higher) and MySQL 8 (or higher) is installed
on your machine.

2. Create a new Python Environment and install the dependent libraries:
```sh
python3 -m venv tma_venv
source tma_venv/bin/activate
pip3 install -r requirements.txt
```
3. Create a new database on your local MySQL server and update the name,
username and password of your database
configuration in the file: test-management-app/test_management_app/settings.py.

4. Run the following command to create initial database setup:
```sh
python3 manage.py migrate
```
5. Import a Backup to your database if you have one.
6. Run the Django Server:
```sh
python3 manage.py runserver
```

## Requirements

Libraries, frameworks and databases used in the project:

* [Django 3.1]() - The web framework for perfectionists with deadlines!
* [Python 3.8]() - Writing Python is faster than speaking.
* [jQuery 3.6]() - Who needs Vanilla Javascript in 2020?
* [MySQL 8]()

## Version
v0.8.0
