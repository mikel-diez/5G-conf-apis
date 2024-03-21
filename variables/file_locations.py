import os
home_directory = os.path.expanduser('~')
PROJ_PATH = home_directory+"/Documents/0_gNB/somo5g"
CONF_FILES = PROJ_PATH+"/configs/"
COMPOSE_FILE = PROJ_PATH+"/docker/docker-compose.yml"
RUN_GNB_SCRIPT = "scripts/rungnb.sh"
COMPOSE_TEMPLATE = "templates/docker-compose.yml"