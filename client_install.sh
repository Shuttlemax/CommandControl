curl -s https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.sh;
chmod +x /root/.cncstartup.sh
curl -s https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.service;

sudo systemctl daemon-reload
sudo systemctl enable cncstartup.service
sudo systemctl start cncstartup.service

sudo systemctl start cncstartup.service