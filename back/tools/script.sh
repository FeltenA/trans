#!/bin/bash

sed -i -r "s/your_db_name/$POSTGRES_DB/1"   /transcendence/transcendence/settings.py
sed -i -r "s/your_db_user/$POSTGRES_USER/1"   /transcendence/transcendence/settings.py
sed -i -r "s/your_db_password/$POSTGRES_PASSWORD/1"   /transcendence/transcendence/settings.py

python /transcendence/manage.py migrate
python /transcendence/manage.py runserver 0.0.0.0:8000