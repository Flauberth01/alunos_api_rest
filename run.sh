#!/bin/sh

python3 manage.py migrate

# shellcheck disable=SC2181
if [ $? -ne 0 ]; then
    echo "Error: migrate failed"
    exit 1
fi

python3 manage.py runserver 0.0.0.0:8000
