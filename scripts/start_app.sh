#!/usr/bin/bash 

sed -i 's/\[]/\["16.171.14.64"]/' /home/ubuntu/blogprojectdrf/blog/settings.py

sudo systemctl start gunicorn
python manage.py migrate 
python manage.py makemigrations     
python manage.py collectstatic
sudo service gunicorn restart
sudo service nginx restart
chmod +x /home/ubuntu/blogprojectdrf/scripts/*.sh
#sudo tail -f /var/log/nginx/error.log
#sudo systemctl reload nginx
#sudo tail -f /var/log/nginx/error.log
#sudo nginx -t
#sudo systemctl restart gunicorn
#sudo systemctl status gunicorn
#sudo systemctl status nginx
# Check the status
#systemctl status gunicorn
# Restart:
#systemctl restart gunicorn
#sudo systemctl status nginx
