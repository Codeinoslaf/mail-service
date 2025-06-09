#!/bin/bash
echo "Старт контейнера"
python manage.py runserver 0.0.0.0:8000 &
exec celery -A mailservice worker --loglevel=info
