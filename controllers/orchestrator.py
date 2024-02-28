import docker

class DockerContainerManager:
    def __init__(self):
        self.client = docker.from_env()

    def get_running_containers(self):
        running_containers = self.client.containers.list()
        return [container.name for container in running_containers]
    

    def execute_command(self, container_name, command):
        container = self.client.containers.get(container_name)
        exit_code, output = container.exec_run(command)
        return output