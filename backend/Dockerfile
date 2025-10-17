FROM python:3.12-slim

# sistem bağımlılıkları (psycopg için)
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# bağımlılıklar
COPY app/requirements.txt /app/app/requirements.txt
RUN pip install --no-cache-dir -r /app/app/requirements.txt

# kod
COPY app /app/app

EXPOSE 8000
