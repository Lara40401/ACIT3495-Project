# ACIT3495-Project1

## Quick Start 
1. Build and start all services:
`docker-compose up --build`
2. Stop all services:
`docker-compose down`

### Dockerfile example:
``` 
# Python: 
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
```