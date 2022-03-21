#!/bin/sh
sudo apt update
sudo apt install docker docker.io docker-compose
sudo docker build -t app .
sudo docker images
sudo docker run -it app

