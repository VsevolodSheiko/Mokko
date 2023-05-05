# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install mysqlclient

# Copy application code
COPY . /app

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 8000

# Start Gunicorn with the appropriate settings
CMD gunicorn Mokko.wsgi:application --config gunicorn.py

