source venv/bin/activate
python3 manage.py migrate >/dev/null
python3 manage.py collectstatic --no-input >/dev/null
