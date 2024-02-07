from fastapi import FastAPI, HTTPException, HTMLResponse, Body, Request
from controllers.enviroment_controller import FileController  
import Jinja2Templates
import json
ENV_FILE = "conf_files/test.env"
app = FastAPI()



templates = Jinja2Templates(directory="templates")


@app.get("/main", response_class=HTMLResponse)
def get_main(request: Request):
    controller = FileController(ENV_FILE)  
    json_info = controller.file_to_dict()
    return templates.TemplateResponse("main.html", {"request": json_info})

@app.get("/get-conf")
def get_configuration():
    controller = FileController(ENV_FILE)  
    return json.loads(controller.to_json())

@app.get("/get-conf/{key}")
def get_specific_configuration(key: str):
    controller = FileController(ENV_FILE)
    return controller.get_value(key)



@app.post("/update-conf")
def update_configuration(config_updates: dict = Body(...)):
    controller = FileController(ENV_FILE)
    try:
        controller.update_config(config_updates)
        return {"message": "Configuration updated successfully for existing keys."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
