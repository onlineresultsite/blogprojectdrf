#!/usr/bin/bash 

cd /home/ubuntu/blogprojectdrf

sed -i 's/\[]/\["13.53.206.233"]/' /home/ubuntu/blogprojectdrf/ecom_app/settings.py


python3 manage.py migrate 
python3 manage.py makemigrations     
python3 manage.py collectstatic
sudo service gunicorn restart
sudo service nginx restart
python3 manage.py runserver 0.0.0.0:8000
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

