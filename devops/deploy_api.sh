#!/bin/bash

ENV_VOL="/home/arraiz/aa_REPOS/PROJ_TKNIKA/TKNIKA_Robotica/.env:/app/conf_files/.env"
DOCKER_SOCK="/var/run/docker.sock:/var/run/docker.sock"
docker build -t 5g_conf_api .
docker run  -p -d 8000:8000 -v $ENV_VOL -v  $DOCKER_SOCK 5g_conf_api:latest


# Ejecuta el script dentro del contenedor y obtiene el PID del proceso
PID=$(bash watchdog.sh)

echo "watchdog PID: $PID"


