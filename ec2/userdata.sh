#!/bin/bash
sudo yum update -y
sudo yum install -y httpd
echo "Apache Installed"
echo "Hello!!!" >> /var/www/html/index.html
sudo systemctl start httpd
echo "Service Started!!!!"