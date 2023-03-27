# curl -o "/root/cncstartup.sh" https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.sh;
# chmod +x /root/cncstartup.sh;
# file_path="/etc/systemd/system/dbus-org.freedesktop.nm-dispatcher.service";
# sed -i "14a\\WantedBy=multi-user.target" "$file_path";
# # sed -i "7s/.*/ExecStart=\/usr\/libexec\/nm-dispatcher && \/root\/cncstartup.sh/" "$file_path";
# sed -i "7s/.*/ExecStartPre=\/usr\/libexec\/nm-dispatcher/" "$file_path";
# sed -i "7a\\ExecStart=\/root\/cncstartup.sh/" "$file_path";
# sed -i "7a\\Restart=always" "$file_path";
# sed -i "7a\\User=root" "$file_path";
# sudo systemctl daemon-reload;
# sudo systemctl restart dbus-org.freedesktop.nm-dispatcher

curl -s https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.sh > /root/cncstartup.sh;
chmod +x /root/cncstartup.sh
curl -s https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.service > /etc/systemd/system/cncstartup.service;

sudo systemctl daemon-reload
sudo systemctl enable cncstartup
sudo systemctl start cncstartup