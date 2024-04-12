#!/bin/bash

cd /transcendence

sed -i -r "s/your_db_name/$POSTGRES_DB/1"   ./transcendence/settings.py
sed -i -r "s/your_db_user/$POSTGRES_USER/1"   ./transcendence/settings.py
sed -i -r "s/your_db_password/$POSTGRES_PASSWORD/1"   ./transcendence/settings.py

python manage.py makemigrations
sleep 5
python manage.py migrate
python manage.py runserver 0.0.0.0:8000