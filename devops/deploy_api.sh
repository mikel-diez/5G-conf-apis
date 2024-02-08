#!/bin/bash

# Inicia el contenedor y obtiene su ID
ENV_VOL=""
DOCKER_SOCK=""
CONTAINER_ID=$(docker run -d 5g_conf_api )

# Ejecuta el script dentro del contenedor y obtiene el PID del proceso
PID=$(bash watchdog.sh)

echo "watchdog PID: $PID"

