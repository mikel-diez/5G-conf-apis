import json
from fastapi import HTTPException
ENV_FILE = "conf_files/test.env"
class FileController:
    def __init__(self, filename):
        self.filename = filename

    def file_to_dict(self):
        data = {}
        with open(self.filename, 'r') as file:
            for line in file:
                key, value = line.strip().split('=', 1)
                key = key.strip()
                value = value.strip().strip('"')
                if value.isdigit():
                    value = int(value)
                else:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                data[key] = value
        return data

   
    def get_value(self, search_key: str):
            data = self.file_to_dict()
            if search_key in data:
                return {search_key: data[search_key]}  # Devuelve directamente el diccionario
            else:
                raise HTTPException(status_code=404, detail="param not in list")
            


    def update_config(self, new_config: dict):
        data = self.file_to_dict()
        updated = False
        
        for key in new_config:
            if key in data:
                data[key] = new_config[key]
                updated = True
        
        if updated:
            with open(self.filename, 'w') as file:
                for k, v in data.items():
                    file.write(f"{k} = {v}\n")

    def to_json(self):
        data = self.file_to_dict()
        return json.dumps(data)
    

# controller = FileController('test.env')
# print(controller.to_json())
# print(controller.get_value("PARAM_C"))
# print(controller.set_value("PARAM_C",20))
# print(controller.to_json())