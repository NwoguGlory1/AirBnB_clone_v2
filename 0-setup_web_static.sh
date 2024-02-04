#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" >> /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu: ubuntu /data/
loc="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n"
sudo sed -i "59i" $loc /etc/nginx/sites-enabled/default
sudo service nginx restart
exit 0
