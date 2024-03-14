import yaml
import json
import os

class YamlToJsonFileController:
    def __init__(self, directory):
        self.directory = directory

    def yaml_to_json(self, filename: str) -> str:
        filepath = os.path.join(self.directory, filename)
        with open(filepath, 'r') as file:
            yaml_data = yaml.safe_load(file)
          
        return json.dumps(yaml_data, indent=2)

    def get_yaml_files(self):
        return [file for file in os.listdir(self.directory) if file.endswith('.yml')]

