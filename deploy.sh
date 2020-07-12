#! /bin/bash
docker-compose build
docker-compose push
scp docker-compose.yaml jenkins@practical-project:/home/jenkins/docker-compose.yaml
ssh jenkins@practical-project	 << EOF
env SECRET_KEY=${SECRET_KEY} env DATABASEB_URI=${DATABASE_URI} env DB_PASSWORD=${DB_PASSWORD} docker stack deploy --compose-file docker-compose.yaml app
EOF
