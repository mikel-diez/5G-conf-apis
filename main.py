from fastapi import FastAPI, HTTPException, Body, Request
from fastapi.responses import HTMLResponse, JSONResponse 

from fastapi.templating import Jinja2Templates
from controllers.yml_controller import YamlToJsonFileController
from controllers.container_controller import DockerComposeConfigReader
from controllers.deployment_controller import DeploymentStatusController
from controllers.gnb_controller import GnbController
from pydantic import BaseModel
from variables.file_locations import COMPOSE_FILE, CONF_FILES
import json
app = FastAPI()


from typing import List

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
    current_yaml = compose_controller.get_gnb_config_file()
    current_yaml = current_yaml.split('/')[-1]
    print(current_yaml)
    yaml_files = controller.get_yaml_files()
    print(yaml_files)
    return templates.TemplateResponse("selector.html", {
    "request": request, 
    "yaml_files": yaml_files, 
    "current_yaml": current_yaml  
})


@app.get("/config/{filename}", response_class=HTMLResponse)
async def get_main(request: Request, filename: str):
    controller = YamlToJsonFileController(CONF_FILES)  
    json_data = controller.yaml_to_json(filename)
    print(json_data)
    print(filename)
    return templates.TemplateResponse("conf_file.html", {
    "request": request, 
    "json_data": json.loads(json_data),
    "filename":filename
})



@app.get("/containerstatus")
def get_container_status():
    containers_json = check_containers()
    return containers_json

@app.get("/deploymentstatus")
def get_container_status():
    status = deployment_status_controller.getStatus()
    if deployment_status_controller is not None:
        deployment_status_controller.setStatus("None") # reset status
    return {"status": status}


@app.post("/update-config/{filename}")
async def update_configuration(request: Request,filename: str,config_updates: dict = Body(...)):
    print(config_updates)
    print(filename)
    controller = YamlToJsonFileController(CONF_FILES)  
    yml_conf=controller.json_to_yml(filename=filename,json_data=config_updates)
    gnb_controller = GnbController()
    gnb_controller.execute_gnb_script("scripts/rungnb.sh")


    

@app.post("/completed")
async def completed(item: Item):
    if item.is_successful not in ["yes", "no"]:
        raise HTTPException(status_code=400, detail="is_successful must be yes or no")
    deployment_status_controller.setStatus("OK")
    status = deployment_status_controller.getStatus()
    print(status)
    print(status)
    return {"status": status}