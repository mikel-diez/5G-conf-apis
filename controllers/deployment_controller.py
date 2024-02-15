class DeploymentStatusController:
    def __init__(self):
        self.__status = None

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status