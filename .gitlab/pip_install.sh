pip install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install --upgrade -q pip
pip3 install --no-cache-dir -qr requirements.txt
