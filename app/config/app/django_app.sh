# Migrate created migrations to database
python manage.py migrate

# Start gunicorn server at port 8000 and keep an eye for app code changes
# If changes occur, kill worker and start a new one
echo worker count = ${WORKER_COUNT}
echo th count = ${TH_COUNT}
gunicorn --reload django-sample.wsgi:application -w ${WORKER_COUNT} -threads ${TH_COUNT} -b 0.0.0.0:8000