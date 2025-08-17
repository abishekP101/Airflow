FROM mcr.microsoft.com/devcontainers/python:3.10

# Install system deps
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Airflow later via postCreateCommand
