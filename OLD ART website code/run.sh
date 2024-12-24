#!/usr/bin/env bash

uwsgi \
  --master \
  --chdir "$(pwd)/src" \
  --pidfile /tmp/server.pid \
  --wsgi-file "$(pwd)/src/project/wsgi.py" \
  --http-socket 0.0.0.0:8000 \
  --honour-range \
  --autoload \
  --tcp-nodelay \
  --vhost-host \
  --processes 2 \
  --threads 2 \
  --post-buffering 204800 \
  --max-requests 5000 \
  --log-date=true \
  --log-slow=true \
  --log-zero \
  --log-4xx \
  --log-5xx \
  --log-ioerror=true \
  --log-sendfile=true \
  --harakiri 30 \
  --harakiri-verbose \
  --http-timeout 300 \
  --socket-timeout 300 \
  --limit-as 768 \
  --die-on-term
