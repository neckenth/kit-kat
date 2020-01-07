# kit-kat
app to expedite process of requesting time-off @ work

## development
* create and activate a new virtualenv and install packages from kit-kat/requirements.txt
* start a local postgres server, create a database entitled `kitkat`, create a user w/ a password, and run migrations to create relations
* add .env file to the project root (kit-kat/mysite) with the same variables as /.env-enxample
* from project root, run local development server: `python3 manage.py runserver`