import subprocess

class GnbController:
    def __init__(self):
        pass

    def execute_gnb_script(self, script_path: str):
        # Construye el comando para ejecutar el script rungnb.
        command = f"bash {script_path}/rungnb"

        # Ejecuta el comando
        try:
            subprocess.run(command, check=True, shell=True, executable='/bin/bash')
            print(f"Script rungnb ha sido ejecutado exitosamente desde: {script_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script rungnb desde {script_path}: {e}")