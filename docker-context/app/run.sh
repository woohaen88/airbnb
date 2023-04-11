#!/bin/sh

set -e

dir=config
if [ ! -d $dir ]; then
    django-admin startproject $dir .
fi

while ! nc $DB_HOST $DB_PORT; do
    >&2 echo "DB is unavailable -- sleeping"
    sleep 1
done

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000