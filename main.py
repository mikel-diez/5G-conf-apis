from fastapi import FastAPI, HTTPException, Body, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from controllers.enviroment_controller import FileController  
from controllers.container_controller import check_containers
from pydantic import BaseModel
from variables.file_locations import ENV_FILE
import json
app = FastAPI()


from typing import List

class Contenedor(BaseModel):
    nombre: str
    estado: str

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def get_main(request: Request):
    controller = FileController(ENV_FILE)  
    json_data = controller.file_to_dict()
    return templates.TemplateResponse("main.html",  {"request": request, "json_data": json_data})

@app.get("/get-conf")
def get_configuration():
    controller = FileController(ENV_FILE)  
    return json.loads(controller.to_json())

@app.get("/get-conf/{key}")
def get_specific_configuration(key: str):
    controller = FileController(ENV_FILE)
    return controller.get_value(key)


@app.get("/status")
def get_container_status():
    containers_json = check_containers()
    return containers_json

@app.post("/update-config")
def update_configuration(config_updates: dict = Body(...)):
    controller = FileController(ENV_FILE)
    try:
        controller.update_config(config_updates)
        return JSONResponse(content={"redirect_url": "/"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
