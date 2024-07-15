#!/usr/bin/bash 

<<<<<<< HEAD
sed -i 's/\[]/\["13.53.206.233"]/' /home/ubuntu/blogprojectdrf/blog/settings.py
=======
sed -i 's/\[]/\["16.171.139.164"]/' /home/ubuntu/blogprojectdrf/blog/settings.py
>>>>>>> 74dcd5938f0e545f65dafc194277bace75993739

python manage.py migrate 
python manage.py makemigrations     
python manage.py collectstatic
sudo service gunicorn restart
sudo service nginx restart
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

