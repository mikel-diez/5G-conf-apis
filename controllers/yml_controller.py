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
    
    def json_to_yml(self, filename: str, json_data: dict) -> str:
        # Asegurarse de que el nombre del archivo termina con '.yml'
        if not filename.endswith('.yml'):
            filename += '.yml'

        filepath = os.path.join(self.directory, filename)
        with open(filepath, 'w') as file:
            yaml.dump(json_data, file, allow_unicode=True)
        
        return f"JSON data has been successfully converted to {filename}"


