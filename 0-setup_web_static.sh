#!/usr/bin/env bash
# prepare web server
sudo -apt-get update
sudo apt -y install nginx
sudo mkdir -p /data/web_static/{shared/,releases/test/}
sudo chown $USER:$USER /data/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -fsn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
service nginx restart
