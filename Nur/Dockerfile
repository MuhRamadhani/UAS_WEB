# Use an official Python runtime as a parent image
FROM python:alpine3.19

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk add --no-cache mariadb-connector-c-dev gcc musl-dev
RUN apk add --no-cache libffi-dev

# Set the working directory in the container
RUN mkdir /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
RUN pip install mysqlclient

# Copy the rest of the application code into the container at /app
COPY . /app/