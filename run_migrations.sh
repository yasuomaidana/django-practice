#!/bin/bash

# Run Django migrations
python manage.py makemigrations
python manage.py migrate