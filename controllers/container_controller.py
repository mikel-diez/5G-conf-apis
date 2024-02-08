import json
from fastapi import HTTPException
import subprocess
import re




def check_containers():
    # comando = ["docker", "ps", "-a", "--format", "{{.Names}}\t{{.Status}}"]
    # resultado = subprocess.run(comando, capture_output=True, text=True)
    # lineas = resultado.stdout.strip().split("\n")
    # contenedores = [{"nombre": linea.split("\t")[0], "estado": linea.split("\t")[1]} for linea in lineas]

    comando = ["docker", "ps", "-a", "--format", "{{.Names}}\t{{.Status}}"]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    lineas = resultado.stdout.strip().split("\n")
    contenedores_dict = [{"nombre": linea.split("\t")[0], "estado": linea.split("\t")[1]} for linea in lineas]
    print(contenedores_dict)
    return (contenedores_dict)