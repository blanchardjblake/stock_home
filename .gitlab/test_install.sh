pip3 install --no-cache-dir -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --no-input
