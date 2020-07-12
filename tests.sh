#! /bin/bash

run apt update
run apt install python3-pip -y

run pip3 install -r service1/requirements.txt

#. /home/muhammad_786_ihsan/DevOps-Practical-Project/venv/bin/activate

cd service1
pytest --cov ./application

cd ../service2
pytest 

cd ../service3
pytest 

cd ../service4
pytest 

