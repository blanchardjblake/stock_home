pip install --upgrade -q pip
pip3 install --no-cache-dir -qr requirements.txt
python3 manage.py migrate >/dev/null
python3 manage.py collectstatic --no-input >/dev/null
