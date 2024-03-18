#!/bin/bash


if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <ruta_al_archivo_config_yml> <ruta_al_docker_compose>"
    exit 1
fi


DOCKER_COMPOSE_FILE=$2


if [ ! -f "$DOCKER_COMPOSE_FILE" ]; then
    echo "Archivo $DOCKER_COMPOSE_FILE no encontrado."
    exit 1
fi


NEW_YML_FILE=$1


if [ ! -f "$NEW_YML_FILE" ]; then
    echo "Archivo $NEW_YML_FILE no encontrado."
    exit 1
fi


ESCAPED_NEW_YML_FILE=$(echo $NEW_YML_FILE | sed 's_/_\\/_g')

# Actualizar la línea en docker-compose.yml
sed -i "/gnb_config.yml:/!b;n;c\    file: ${ESCAPED_NEW_YML_FILE}" $DOCKER_COMPOSE_FILE

echo "El archivo $DOCKER_COMPOSE_FILE ha sido actualizado."

# Ejecutar Docker Compose
docker compose -f $DOCKER_COMPOSE_FILE up -d --force-recreate
