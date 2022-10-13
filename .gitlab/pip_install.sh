pip3 install --root-user-action=ignore -r virtualenv
virtualenv venv
source venv/bin/activate
pip3 install --upgrade -q pip
pip3 install --no-cache-dir -qr requirements.txt
