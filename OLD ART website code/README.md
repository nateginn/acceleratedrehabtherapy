# acceleratedrehabtherapy.com

Recommended: Deploy on Debian (any version) and use Python versions 3.7-3.9.

## Install Required Packages
```bash
sudo apt-get install -y git make gcc g++ postgresql postgresql-client libpq-dev \
    libjpeg-dev libpng-dev libwebp-dev libgif-dev libtiff-dev zlib1g-dev \
    libxml2-dev libxslt1-dev redis-server redis-tools
```

## Create Project Directory and Extract Files
```bash
mkdir acceleratedrehabtherapy.com
tar -xf ./acceleratedrehabtherapy.com.tar -C ./acceleratedrehabtherapy.com
cd acceleratedrehabtherapy.com
```

## Restore Database
```bash
createdb acceleratedrehabtherapy.com
gunzip -c ./backup/acceleratedrehabtherapy.com.2024-09-05.sql.gz \
  | grep -v -E '(DROP\ EXTENSION|CREATE\ EXTENSION|DROP\ SCHEMA|CREATE\ SCHEMA|COMMENT\ ON)' \
  | psql -v ON_ERROR_STOP=on --single-transaction --dbname=acceleratedrehabtherapy.com
```

## Create Virtual Environment
```bash
python3.7 -m venv --prompt=acceleratedrehabtherapy.com .venv
. .venv/bin/activate
pip install -r requirements/dev.txt
```

## Run Development Server

Configure database credentials in the `src/settings/dev.py`.

```bash
export DJANGO_SETTINGS_MODULE=settings.dev
python3 src/manage.py collectstatic --clear --noinput
python3 src/manage.py runserver
```

## Run Production Server

1. Configure `EMAIL_*` settings in the `src/settings/common.py`.
2. Set the absolute path to the site root folder in the `PROJECT_ROOT` variable in the `src/settings/production.py`.

> For serving static files, it's recommended to use Nginx as a reverse proxy.
> An example configuration file can be found at `nginx.example.conf`.

```bash
pip install uwsgi
export DB_HOST=localhost DB_NAME=acceleratedrehabtherapy.com DB_USER=user DB_PASS=password
python3 src/manage.py collectstatic --clear --noinput
./run.sh
```
