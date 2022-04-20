@echo off

Rem Delete old database
del db.sqlite3

Rem Load static files
python manage.py collectstatic --noinput

Rem Check for any project errors
python manage.py check

Rem Run Django migrations to create database tables
python manage.py migrate

Rem Populate the database with dummy data
python scripts/populate_database.py

Rem Run the development server
start /b python manage.py runserver

Rem Open browser
timeout /t 2
start http://127.0.0.1:8000/