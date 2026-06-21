# Imagen base liviana con Python 3.11
FROM python:3.11-slim

# Evita que Python escriba .pyc y bufferee la salida (mejor para logs)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependencias del sistema necesarias para psycopg2 (PostgreSQL)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalar dependencias de Python primero (aprovecha la cache de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el codigo del proyecto
COPY . .

# Script de arranque (migraciones + estaticos + gunicorn)
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]