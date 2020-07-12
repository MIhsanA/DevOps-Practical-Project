#! /bin/bash

sudo apt update
sudo apt install python3-pip -y

pip3 install -r service1/requirements.txt
pip3 install pytest pytest-cov
#. /home/muhammad_786_ihsan/DevOps-Practical-Project/venv/bin/activate

cd service1
python3 -m pytest --cov ./application

cd ../service2
python3 -m pytest 

cd ../service3
python3 -m pytest 

cd ../service4
python3 -m pytest 

