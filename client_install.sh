#!/bin/bashd
curl -s https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.sh > /root/cncstartup.sh;
chmod +x /root/cncstartup.sh
curl -s https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.service > /etc/systemd/system/cncstartup.service;

sudo systemctl daemon-reload
sudo systemctl enable cncstartup
sudo systemctl start cncstartup