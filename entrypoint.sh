#!/bin/sh
set -e

echo "Esperando a la base de datos..."
# Pequena espera para que PostgreSQL este listo
sleep 3

echo "Aplicando migraciones..."
python manage.py migrate --noinput

echo "Recolectando archivos estaticos..."
python manage.py collectstatic --noinput

echo "Iniciando gunicorn..."
exec gunicorn agro.wsgi:application --bind 0.0.0.0:8000 --workers 3