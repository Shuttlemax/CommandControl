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

sudo nmcli con mod enp0s3 ipv4.dns "8.8.8.8 8.8.4.4"
sudo systemctl restart NetworkManager

curl -s https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.sh > /etc/cncstartup.sh;
chmod +x /etc/cncstartup.sh
# curl -s https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.service > /etc/systemd/system/cncstartup.service;

cat "@reboot root /etc/cncstartup.sh >> /etc/startuplog 2>&1" >> /etc/crontab
touch /etc/startuplog
echo "Rebooting system to finish installation"
reboot