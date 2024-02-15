import subprocess
import json
import requests
import time
API_ENPOINT_REQUEST = "http://localhost:8000/containerstatus"
CONTAINER_TO_MATCH = "saha"
API_SIGNAL_REQUEST = "http://localhost:8000/completed"
SCRIPT = "/home/arraiz/aa_REPOS/PROJ_TKNIKA/TKNIKA_Robotica/API/scripts/run_containers.sh"
def check_containers():
    response = requests.get(API_ENPOINT_REQUEST)
    print(json.loads(response.content))
    if response.content is not None:
        json_resp=json.loads(response.content)
    
        for l in json_resp:
            for k,v in l.items(): # k: "nombre" v: "container_name" is the container name
                if CONTAINER_TO_MATCH in v: # got match
                    # kill and restart the container
                    result = subprocess.run(['bash', '-c', SCRIPT], capture_output=True, text=True)
                    salida_estandar = result.stdout
                    salida_error = result.stderr
                    print(salida_error)
                    print(salida_estandar)
                    
                    time.sleep(1)
                    # if we got an error
                    if salida_error is not None:
                        data = {"is_successful": "no"}
                    # send signal to the api
                    data = {"is_successful": "yes"} 
                    print(data)
                    response = requests.post(API_SIGNAL_REQUEST, json=data)

if __name__ == "__main__":
    check_containers()