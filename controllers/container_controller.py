import yaml
from variables.file_locations import COMPOSE_FILE
import re

class DockerComposeConfigReader:
    def __init__(self, docker_compose_path):
        self.docker_compose_path = docker_compose_path

    def get_gnb_config_file(self):
        with open(self.docker_compose_path, 'r') as file:
            docker_compose_content = yaml.safe_load(file)
        
        config_path = None
        core_ip = "192.199.1.30"  # Un valor predeterminado
        gnb_ip = "192.199.1.37"   # Un valor predeterminado

        # Extraer la ruta del archivo de configuración
        if 'configs' in docker_compose_content and 'gnb_config' in docker_compose_content['configs']:
            config_path = docker_compose_content['configs']['gnb_config'].get('file', None)

        # Extraer las direcciones IP desde la línea de comando
        if 'services' in docker_compose_content and 'gnb' in docker_compose_content['services']:
            command = docker_compose_content['services']['gnb'].get('command', '')
            core_ip_match = re.search(r"\${OPEN5GS_IP:-([\d\.]+)}", command)
            gnb_ip_match = re.search(r"\${GNB_IP:-([\d\.]+)}", command)
            
            if core_ip_match:
                core_ip = core_ip_match.group(1)
            if gnb_ip_match:
                gnb_ip = gnb_ip_match.group(1)
        # Devolver None si no se encuentra el path de configuración
        if config_path is None:
            return None, core_ip, gnb_ip
        return [config_path, core_ip, gnb_ip]
