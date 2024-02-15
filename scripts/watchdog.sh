#!/bin/bash

FILE_TO_WATCH_PATH="/home/arraiz/aa_REPOS/PROJ_TKNIKA/TKNIKA_Robotica/API/conf_files/.env"
SCRIPT_TO_RUN="/home/arraiz/aa_REPOS/PROJ_TKNIKA/TKNIKA_Robotica/API/scripts/restart_env.py"

# Monitorear cambios en el archivo
inotifywait -m -e close_write --format "%w%f" "${FILE_TO_WATCH_PATH}" | while read FILE
do
    echo "Archivo ha sido modificado."
    python3 ${SCRIPT_TO_RUN}
done