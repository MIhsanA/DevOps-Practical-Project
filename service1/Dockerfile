# Derived from official mysql image (our base image)
#FROM mysql
# Add a database
# Add the content of the .sql file to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
#COPY CreateTable.sql /docker-entrypoint-initdb.d/
#EXPOSE 3306
#Use Python Image
From python:3.8
# Install apt dependencies
Run apt update
Run apt install python3-pip -y
# Copy contents into image
Copy . .
# run pip dependencies
Run pip3 install -r requirements.txt 
# Expose correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT [ "/usr/local/bin/python3", "app.py" ]
