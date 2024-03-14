#!/bin/bash

ENV_VOL="/home/telecomunicaciones/Documents/0_gNB/somo5g/configs/:/app/conf_files/"
COMPOSE_VOL="/home/telecomunicaciones/Documents/0_gNB/somo5g/docker:/app/docker/"
DOCKER_SOCK="/var/run/docker.sock:/var/run/docker.sock"
docker container rm --force 5g_conf_api
docker build -t 5g_conf_api .
docker run  -p  8000:8000 -v $ENV_VOL -v $COMPOSE_VOL -v $DOCKER_SOCK  --name "5g_conf_api" 5g_conf_api:latest 


# Ejecuta el script dentro del contenedor y obtiene el PID del proceso
#PID=$(bash watchdog.sh)

#echo "watchdog PID: $PID"


