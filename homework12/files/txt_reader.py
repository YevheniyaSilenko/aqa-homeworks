from interfaces.iread import Read


class TxtReader(Read):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def read(self):
        with open(self.__file_path, 'r') as file:
            return file.read()
