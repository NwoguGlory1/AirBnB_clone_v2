#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Holberton School" >> sudo tee /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "Chown completed successfully"
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
} " | sudo tee /etc/nginx/sites-available/default
sudo nginx -t && sudo service nginx restart
exit 0
