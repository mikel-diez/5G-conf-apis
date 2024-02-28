import yaml
import json

class YamlToJsonFileController:
    def __init__(self, filename):
        self.filename = filename

    def yaml_to_json(self) -> str:
        with open(self.filename, 'r') as file:
            yaml_data = yaml.safe_load(file)
          
        return json.dumps(yaml_data, indent=2)
    



if __name__ == "__main__":
    controller = YamlToJsonFileController("/home/arraiz/aa_REPOS/PROJ_TKNIKA/TKNIKA_Robotica/API/conf_files/config.yml")
    controller.yaml_to_json()