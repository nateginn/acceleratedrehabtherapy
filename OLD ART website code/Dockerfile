FROM python:3.7-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    postgresql-client \
    libpq-dev \
    libjpeg-dev \
    libpng-dev \
    libwebp-dev \
    libgif-dev \
    libtiff-dev \
    zlib1g-dev \
    libxml2-dev \
    libxslt1-dev \
    sassc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements/common.txt requirements/common.txt
COPY requirements/production.txt requirements/production.txt

RUN pip install -r requirements/production.txt
RUN pip install uwsgi

COPY . .

# Make sure the run script is executable
RUN chmod +x run.sh

EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=settings.dev_common
ENV PYTHONPATH=/app/src

# Run the application
CMD ["./run.sh"]