#!/bin/bash

FILE_PATH=""
SCRIPT_TO_RUN=""

# Monitorear cambios en el archivo
inotifywait -m -e close_write --format "%w%f" "${FILE_PATH}" | while read FILE
do
    echo "Archivo ${FILE} ha sido modificado."
    bash "${SCRIPT_TO_RUN}"
done