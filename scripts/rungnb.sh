#!/bin/bash

# Comprobar si se proporcionaron dos argumentos
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <ruta_al_archivo_config_yml> <ruta_al_docker_compose>"
    exit 1
fi

# El archivo Docker Compose proporcionado como segundo argumento
DOCKER_COMPOSE_FILE=$2

# Comprobar si el archivo Docker Compose existe
if [ ! -f "$DOCKER_COMPOSE_FILE" ]; then
    echo "Archivo $DOCKER_COMPOSE_FILE no encontrado."
    exit 1
fi

# El nuevo archivo de configuración YML proporcionado como primer argumento
NEW_YML_FILE=$1

# Comprobar si el nuevo archivo YML existe
if [ ! -f "$NEW_YML_FILE" ]; then
    echo "Archivo $NEW_YML_FILE no encontrado."
    exit 1
fi

# Escapar la ruta del nuevo archivo YML para usar en sed
ESCAPED_NEW_YML_FILE=$(echo $NEW_YML_FILE | sed 's_/_\\/_g')

# Actualizar la línea en docker-compose.yml
sed -i "/gnb_config.yml:/!b;n;c\    file: ${ESCAPED_NEW_YML_FILE}" $DOCKER_COMPOSE_FILE

echo "El archivo $DOCKER_COMPOSE_FILE ha sido actualizado."

# Ejecutar Docker Compose
docker compose -f $DOCKER_COMPOSE_FILE up -d --force-recreate
