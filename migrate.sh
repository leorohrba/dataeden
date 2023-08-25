#!/bin/bash

set -e

echo "Running migrations."
python manage.py makemigrations --merge
python manage.py migrate --noinput

echo "Collecting static."
python manage.py collectstatic --noinput

echo "Compressing static."
python /app/manage.py compress --force

# Start the Django application.
python manage.py runserver 0.0.0.0:8000