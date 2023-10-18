#!/bin/bash
if [ "$DATABASE" = "postgres" ]
then 
    echo "waiting for postgres.."

    while ! nc -z $DATABASE_HOSTNAME $DATABASE_PORT; do 
        sleep 0.1 
    done 

    echo "postgresql started"

fi 

# python manage.py flush --no-input
# python manage.py migrate

exec "$@"