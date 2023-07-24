sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/default
sudo cp ~/web/etc/nginx.conf /etc/nginx/sites-available/test.conf
sudo ln -s /etc/nginx/sites-available/test.conf /etc/nginx/sites-enabled/
sudo nginx -t
