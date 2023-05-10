# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install mysqlclient

# Copy application code
COPY . .

# Set working directory
WORKDIR /app
#ENTRYPOINT celery -A Mokko worker --loglevel=INFO

# Expose port
EXPOSE 8000

# Start Gunicorn with the appropriate settings
#CMD gunicorn -c gunicorn.py Mokko.wsgi 

