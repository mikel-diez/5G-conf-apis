from fastapi import FastAPI, HTTPException, Body, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from controllers.enviroment_controller import FileController  
from controllers.yml_controller import YamlToJsonFileController
from controllers.container_controller import check_containers
from controllers.deployment_controller import DeploymentStatusController
from pydantic import BaseModel
from variables.file_locations import ENV_FILE, YML_FILE
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

# @app.get("/", response_class=HTMLResponse)
# def get_main(request: Request):
#     controller = FileController(ENV_FILE)  
#     json_data = controller.file_to_dict()
#     return templates.TemplateResponse("main.html",  {"request": request, "json_data": json_data})

@app.get("/", response_class=HTMLResponse)
def get_main(request: Request):
    controller = YamlToJsonFileController(YML_FILE)  
    json_data = controller.yaml_to_json()
    return templates.TemplateResponse("main.html",  {"request": request, "json_data": json.loads(json_data)})


@app.get("/get-conf")
def get_configuration():
    controller = FileController(ENV_FILE)  
    return json.loads(controller.to_json())

@app.get("/get-conf/{key}")
def get_specific_configuration(key: str):
    controller = FileController(ENV_FILE)
    return controller.get_value(key)


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


@app.post("/update-config")
def update_configuration(config_updates: dict = Body(...)):
    controller = FileController(ENV_FILE)
    try:
        controller.update_config(config_updates)
        return JSONResponse({"status":"pending"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/completed")
async def completed(item: Item):
    if item.is_successful not in ["yes", "no"]:
        raise HTTPException(status_code=400, detail="is_successful must be yes or no")
    deployment_status_controller.setStatus("OK")
    status = deployment_status_controller.getStatus()
    print(status)
    print(status)
    return {"status": status}