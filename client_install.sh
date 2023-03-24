curl -o setup.py https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.sh;
chmod +x /root/.auto-update-check
curl -o setup.py https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.service;

sudo systemctl daemon-reload
sudp systemctl enable cnstartup.service
sudo systemctl start cnstartup.service

sudo systemctl start cncstartup.service