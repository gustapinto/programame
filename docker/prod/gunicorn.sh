#!/bin/sh
cd src && gunicorn --reload --bind 0.0.0.0:8000 src.wsgi
