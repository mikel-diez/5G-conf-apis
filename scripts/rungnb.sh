#!/bin/bash

# Verificar que se recibieron cuatro argumentos.
if [ "$#" -ne 4 ]; then
    echo "Uso: $0 <ruta_al_archivo_config_yml> <ruta_al_docker_compose> <IP del GNB> <IP del Core>"
    exit 1
fi

CONFIG_PATH=$1
DOCKER_COMPOSE_PATH=$2
GNB_IP=$3
CORE_IP=$4

# Detener y eliminar el contenedor si ya existe.
CONTAINER_ID=$(docker ps -q -f name=srsran_gnb)
if [ ! -z "$CONTAINER_ID" ]; then
    echo "Deteniendo y eliminando el contenedor existente srsran_gnb..."
    docker stop srsran_gnb
    docker rm srsran_gnb
fi

# Reemplazar los valores predeterminados de las IPs en el comando dentro del docker-compose.
sed -i "s|amf --addr \${OPEN5GS_IP:-[0-9\.]*}|amf --addr \${OPEN5GS_IP:-$CORE_IP}|" $DOCKER_COMPOSE_PATH
sed -i "s|--bind_addr \${GNB_IP:-[0-9\.]*}|--bind_addr \${GNB_IP:-$GNB_IP}|" $DOCKER_COMPOSE_PATH

# Eliminar la ruta del archivo de configuración existente y añadir la nueva.
sed -i "/gnb_config.yml:/!b;n;c\    file: $CONFIG_PATH" $DOCKER_COMPOSE_PATH

# Navegar al directorio donde se encuentra docker-compose.yml y ejecutar docker compose.
cd $(dirname $DOCKER_COMPOSE_PATH)
docker compose -f $(basename $DOCKER_COMPOSE_PATH) up -d

echo "Docker Compose ha sido ejecutado."
