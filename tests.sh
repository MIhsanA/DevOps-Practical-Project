#! /bin/bash

. /home/muhammad_786_ihsan/DevOps-Practical-Project/venv/bin/activate

cd /home/jenkins/.jenkins/workspace/DevOps-Practical-Project/service1
pytest --cov ./application

cd /home/jenkins/.jenkins/workspace/DevOps-Practical-Project/service2
pytest 

cd /home/jenkins/.jenkins/workspace/DevOps-Practical-Project/service3
pytest 

cd /home/jenkins/.jenkins/workspace/DevOps-Practical-Project/service4
pytest 

