#!/bin/sh


echo "---- init database ----"

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done

echo "✅ database has initialized successfully ✅"
fi

exec "$@"
