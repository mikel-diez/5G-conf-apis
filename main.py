from fastapi import FastAPI, HTTPException, Body, Request
from fastapi.responses import HTMLResponse, JSONResponse 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from controllers.yml_controller import YamlToJsonFileController
from controllers.container_controller import DockerComposeConfigReader
from controllers.deployment_controller import DeploymentStatusController
from controllers.gnb_controller import GnbController
from pydantic import BaseModel
from variables.file_locations import COMPOSE_FILE, CONF_FILES, RUN_GNB_SCRIPT
import json
import os
from typing import List


app = FastAPI()

directory = "static"
absolute_directory_path = os.path.abspath(directory)


if not os.path.exists(absolute_directory_path):
    os.makedirs(absolute_directory_path)

app.mount("/static", StaticFiles(directory=absolute_directory_path), name="static")



class Contenedor(BaseModel):
    nombre: str
    estado: str

class Item(BaseModel):
    is_successful: str

templates = Jinja2Templates(directory="templates")


deployment_status_controller = DeploymentStatusController()



@app.get("/", response_class=HTMLResponse)
async def get_main(request: Request):
    controller = YamlToJsonFileController(CONF_FILES)  
    compose_controller = DockerComposeConfigReader(COMPOSE_FILE)
    current_yaml,core_ip,gnb_ip = compose_controller.get_gnb_config_file()
    if current_yaml is not None:
        current_yaml = current_yaml.split('/')[-1]
    print(current_yaml)
    yaml_files = controller.get_yaml_files()
    print(core_ip)
    print(gnb_ip)
    return templates.TemplateResponse("selector.html", {
    "request": request, 
    "yaml_files": yaml_files, 
    "current_yaml": current_yaml,
    "core_ip":core_ip,
    "gnb_ip":gnb_ip
})


@app.get("/config/{filename}", response_class=HTMLResponse)
async def get_main(request: Request, filename: str, core_ip:str, gnb_ip:str):
    controller = YamlToJsonFileController(CONF_FILES)  
    json_data = controller.yaml_to_json(filename)
    print(json_data)
    print(filename)
    return templates.TemplateResponse("conf_file.html", {
    "request": request, 
    "json_data": json.loads(json_data),
    "filename":filename,
    "core_ip":core_ip,
    "gnb_ip":gnb_ip
})

@app.get("/deploymentstatus")
def get_container_status():
    status = deployment_status_controller.getStatus()
    if deployment_status_controller is not None:
        deployment_status_controller.setStatus("None") # reset status
    return {"status": status}


@app.post("/update-config/{filename}")
async def update_configuration(request: Request,core_ip: str, gnb_ip: str,filename: str,config_updates: dict = Body(...)):
    
    controller = YamlToJsonFileController(CONF_FILES)
        
    if not filename.endswith('.yml'):
        filename += '.yml'
    
    conf_file = controller.json_to_yml(filename=filename, json_data=config_updates)
    gnb_controller = GnbController(RUN_GNB_SCRIPT)
    gnb_controller.execute_gnb_script(CONF_FILES+conf_file, COMPOSE_FILE, gnb_ip, core_ip)
    return {"satus":"stats"}


    

