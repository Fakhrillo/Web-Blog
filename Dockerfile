FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies for Postgres and build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --no-cache-dir uv

# Copy the project files
COPY . .

# Install dependencies
RUN uv sync

RUN uv run manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Default command: migrate and start Gunicorn
CMD ["/bin/sh", "-c", "uv run manage.py migrate && uv run gunicorn mysite.wsgi:application --access-logfile - --bind 0.0.0.0:8000"]