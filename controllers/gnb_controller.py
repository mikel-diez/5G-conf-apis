import subprocess

class GnbController:
    def __init__(self, script_path):
        self.script_path = script_path

    def execute_gnb_script(self, config_path, docker_compose_path, gnb_ip, core_ip):
        
        command = f"{self.script_path} {config_path} {docker_compose_path} {gnb_ip} {core_ip}"

        try:
            subprocess.run(command, check=True, shell=True, executable='/bin/bash')
            print("Script rungnb ha sido ejecutado exitosamente con los parámetros proporcionados")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script rungnb: {e}")
