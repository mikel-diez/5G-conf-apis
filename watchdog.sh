#!/bin/bash

FILE_PATH="/home/arraiz/aa_REPOS/PROJ_TKNIKA/TKNIKA_Robotica/test.env"
SCRIPT_TO_RUN="update_env.sh"

# Monitorear cambios en el archivo
inotifywait -m -e close_write --format "%w%f" "${FILE_PATH}" | while read FILE
do
    echo "Archivo ${FILE} ha sido modificado."
    # Ejecutar otro script o comando
    bash "${SCRIPT_TO_RUN}"
done