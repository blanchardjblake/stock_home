pip3 install --root-user-action=ignore -q virtualenv
virtualenv venv
source venv/bin/activate
pip3 install --upgrade -q pip
pip3 install --no-cache-dir -qr requirements.txt
python3 manage.py migrate >/dev/null
python3 manage.py collectstatic --no-input >/dev/null
