#!/bin/sh
gunicorn main:app --chdir app -w 2 --threads 2 -b 0.0.0.0:8000 --reload
exec "$@"
