#!/bin/bash

if [ -n "$SYSTEM_ENV" ]
then
  if [ "$SYSTEM_ENV" == "PRODUCTION" ]
  then
    exec gunicorn --bind "0.0.0.0:$PORT" --workers 2 --threads 8 --timeout 0 core.wsgi:application --env DJANGO_SETTINGS_MODULE=apolloapi.settings.production
    exit
  else
    exec gunicorn --bind "0.0.0.0:$PORT" --workers 2 --threads 8 --timeout 0 core.wsgi:application --env DJANGO_SETTINGS_MODULE=apolloapi.settings.local
    exit
  fi
else
  echo -e "SYSTEM_ENV not set\n"
fi
