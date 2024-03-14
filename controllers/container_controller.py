import yaml
from variables.file_locations import COMPOSE_FILE

class DockerComposeConfigReader:
    def __init__(self, docker_compose_path):
        self.docker_compose_path = docker_compose_path

    def get_gnb_config_file(self):
        with open(self.docker_compose_path, 'r') as file:
            docker_compose_content = yaml.safe_load(file)
        
        # Asegúrate de que las claves 'configs' y 'gnb_config.yml' existan
        if 'configs' in docker_compose_content and 'gnb_config.yml' in docker_compose_content['configs']:
            config_path = docker_compose_content['configs']['gnb_config.yml'].get('file', None)
            if config_path is not None:
                # Extrae el valor predeterminado si está presente
                if config_path.startswith('${') and ':-' in config_path:
                    return config_path.split(':-')[1].rstrip('}')
                return config_path
        return None
