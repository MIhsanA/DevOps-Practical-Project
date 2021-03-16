# DevOps-Practical-Project  Hasan
**DevOps Practical Project**
Contents
•	Objective
•	Overview
•	Planning
•	Technology’s Used
•	Database
•	CI Pipeline/Deployment
•	Risk Assessment
•	Testing
•	Current Issues
•	Improvements

**Objective**
To create an application that creates 'Objects' that is made from a set of predefined rules. This will have to be accomplished using the technologies and methodologies taught.
Make flask app based on 4 services Communication with API. 
**Overview**
	Service 1 will get a number from secice2 and get a person from database where ID is equal to the number. Then get type of car from service 3 and colour of the car will be decided by service4 base on the first letter of the name. and all the information is displayed. I used SQL image for my database from Docker.
**Planning**
 
![image](https://user-images.githubusercontent.com/65769901/87277725-c1b4fd00-c4da-11ea-944b-86f768475e22.png)
Trello is, at its core, an online corkboard. You use it to organize “cards” into lists—those cards can be tasks, notes, projects, shared files, or anything else that helps
I used Trello for planning my app. 
![image](https://user-images.githubusercontent.com/65769901/87278389-3d637980-c4dc-11ea-8f7c-be3b0d54ef7b.png)

**Database**
Table design for SQL
![image](https://user-images.githubusercontent.com/65769901/87278414-4d7b5900-c4dc-11ea-96de-9c1452ad3e36.png)

**Technology’s Used**
![image](https://user-images.githubusercontent.com/65769901/87278448-62f08300-c4dc-11ea-881c-f10abb2ed40b.png)
**Flask** is a Python-based micro web framework which allows you to write your web applications quickly and efficiently

**Jinja2** is a template engine written in pure Python. It provides a Django-inspired non-XML syntax but supports inline expressions and an optional sandboxed environment.

The **Flask response** class,Flask uses it internally as a container for the response data returned by application route functions, plus some additional information needed to create an HTTP response

**Flask Unit Testing**
Flask provides a way to test your application by exposing the Werkzeug test Client and handling the context locals for you. You can then use that with your favourite testing solution
![image](https://user-images.githubusercontent.com/65769901/87278556-aea32c80-c4dc-11ea-962e-b211cff5ca71.png)
**Pytest** is a testing framework which allows us to write test codes using python. You can write code to test anything like database , API, even UI if you want. But pytest is mainly being used in industry to write tests for APIs.
![image](https://user-images.githubusercontent.com/65769901/87278576-b9f65800-c4dc-11ea-9112-6e08ca2577fa.png)
Mocking external components. Mock testing is an approach to unit testing that lets you make assertions about how the code under test is interacting with other system modules. In mock testing, the dependencies are replaced with objects that simulate the behaviour of the real ones
**Docker**
![image](https://user-images.githubusercontent.com/65769901/87278603-caa6ce00-c4dc-11ea-954f-106e8de62d42.png)
 Docker is an open-source project that automates the deployment of applications inside software containers, by providing an additional layer of abstraction and automation of operating-system-level virtualization on Linux. Docker uses resource isolation features of the Linux kernel such as cgroups and kernel namespaces to allow independent “containers” to run within a single Linux instance, avoiding the overhead of starting and maintaining virtual machines.

A **Docker container image** is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.
•	SQL image used for Database container 

**Docker Compose** is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. Compose works in all environments: production, staging, development, testing, as well as CI workflows.

**Docker Swarm** is native clustering for Docker. It turns a pool of Docker hosts into a single, virtual Docker host. Because Docker Swarm serves the standard Docker API, any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts.

The **Docker Hub** is a cloud-based registry service for building and shipping application or service containers. It provides a centralized resource for container image discovery, distribution and change management, user and team collaboration, and workflow automation throughout the development pipeline.

**GitHub**
![image](https://user-images.githubusercontent.com/65769901/87278715-0b9ee280-c4dd-11ea-81d3-299a5390c78e.png)
 GitHub is a web-based Git repository hosting service, which offers all of the distributed revision control and source code management (SCM) functionality of Git as well as adding its own features. Unlike Git, which is strictly a command-line tool, GitHub provides a web-based graphical interface and desktop as well as mobile integration
![image](https://user-images.githubusercontent.com/65769901/87278735-1194c380-c4dd-11ea-97e7-4910bcea45f9.png)
 **Ansible** is an open-source software platform for configuring and managing computers. It combines multi-node software deployment, ad hoc task execution, and configuration management. It manages nodes over SSH or PowerShell and requires Python (2.4 or later) to be installed on them. Modules work over JSON and standard output and can be written in any programming language. The system uses YAML to express reusable descriptions of systems.
![image](https://user-images.githubusercontent.com/65769901/87278755-1fe2df80-c4dd-11ea-8311-600d850e1dbb.png)
 **Jenkins** is an open source continuous integration tool written in Java. Jenkins provides continuous integration services for software development. It is a server-based system running in a servlet container such as Apache Tomcat. It supports SCM tools including AccuRev, CVS, Subversion, Git, Mercurial, Perforce, Clearcase and RTC, and can execute Apache Ant and Apache Maven based projects as well as arbitrary shell scripts and Windows batch commands.
![image](https://user-images.githubusercontent.com/65769901/87278778-2f622880-c4dd-11ea-9470-cdf5ea142054.png)
**NGINX** is open source software for web serving, reverse proxying, caching, load balancing, media streaming, and more. ... In addition to its HTTP server capabilities, NGINX can also function as a proxy server for email (IMAP, POP3, and SMTP) and a reverse proxy and load balancer for HTTP, TCP, and UDP servers.
![image](https://user-images.githubusercontent.com/65769901/87278801-3ee17180-c4dd-11ea-92bd-281c061d15c9.png)
 Google Cloud Platform offers services for compute, storage, networking, big data, machine learning and the internet of things (IoT), as well as cloud management, security and developer tools. ... Google Cloud Storage, which is a cloud storage platform designed to store large, unstructured data sets

**CI Pipeline/Deployment**
![image](https://user-images.githubusercontent.com/65769901/87278835-5882b900-c4dd-11ea-83b0-088e2c2bdf01.png)

Final ci pipeline
![image](https://user-images.githubusercontent.com/65769901/87278860-66383e80-c4dd-11ea-931a-37c91d598a35.png)

**Risk Assessment**
[](https://docs.google.com/spreadsheets/d/1kJK4JxCoMXqOS6U0VTs0-iOHTLHc1YL_pbm0T2j-Tmc/edit#gid=0
) 
![image](https://user-images.githubusercontent.com/65769901/87278891-7f40ef80-c4dd-11ea-988f-0ecdf7c5fc20.png)

**Testing**
 
![image](https://user-images.githubusercontent.com/65769901/87278903-8bc54800-c4dd-11ea-853c-9a30b849cc59.png)

![image](https://user-images.githubusercontent.com/65769901/87278915-9384ec80-c4dd-11ea-8298-c3bfa95e30c4.png)

 
**Current Issues**
Service1 is giving from fix amount of numbers. 

**Improvement**
Service1 should random from total number of names in database 
