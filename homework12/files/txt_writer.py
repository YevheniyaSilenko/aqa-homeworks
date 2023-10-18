from interfaces.iwrite import Write

class TxtWriter(Write):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def write(self, data):
        with open(self.__file_path, 'w') as file:
            file.write(data)
