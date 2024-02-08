#!/bin/bash

# Inicia el contenedor y obtiene su ID
ENV_VOL=""
ENV_VOL="/home/arraiz/aa_REPOS/PROJ_TKNIKA/TKNIKA_Robotica/.env:/app/conf_files/.env"
DOCKER_SOCK="/var/run/docker.sock:/var/run/docker.sock"

CONTAINER_ID=$(docker run -d -v $ENV_VOL -v $DOCKER_SOCK 5g_conf_api)
echo "Contenedor lanzado con ID: $CONTAINER_ID"


# Ejecuta el script dentro del contenedor y obtiene el PID del proceso
PID=$(bash watchdog.sh)

echo "watchdog PID: $PID"

