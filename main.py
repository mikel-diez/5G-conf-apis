from fastapi import FastAPI, HTTPException, Body, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from controllers.enviroment_controller import FileController  

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


@app.post("/status")
async def actualizar_status(contenedores: List[Contenedor]):
    for contenedor in contenedores:
        # Aquí podrías procesar cada contenedor según necesites
        print(f"Contenedor: {contenedor.nombre}, Estado: {contenedor.estado}")
    return {"mensaje": "Status de contenedores actualizado"}

@app.post("/update-config")
def update_configuration(config_updates: dict = Body(...)):
    controller = FileController(ENV_FILE)
    try:
        controller.update_config(config_updates)
        return JSONResponse(content={"redirect_url": "/"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
