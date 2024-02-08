import subprocess
import json
import requests

def check_containers():
    comando = ["docker", "ps", "-a", "--format", "{{.Names}}\t{{.Status}}"]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    lineas = resultado.stdout.strip().split("\n")
    contenedores = [{"nombre": linea.split("\t")[0], "estado": linea.split("\t")[1]} for linea in lineas]
    json_data = json.dumps(contenedores)
    print(json_data)
    #response = requests.post("http://tuapi.com/status", data=json_data, headers={"Content-Type": "application/json"})
    #(response.text)

if __name__ == "__main__":
    check_containers()