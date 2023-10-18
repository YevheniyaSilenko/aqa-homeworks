from interfaces.iread import Read
from interfaces.iwrite import Write
from txt_reader import TxtReader
from txt_writer import TxtWriter

class ProxyTxtRW(Read, Write):
    def __init__(self, real_reader: Read, real_writer: Write):
        self.__result = ''
        self.__is_actual = None
        self.__real_reader = real_reader
        self.__real_writer = real_writer

    def read(self):
        if self.__is_actual is None:
            self.__result = self.__real_reader.read()
            self.__is_actual = True
        return self.__result

    def write(self, data):
        self.__real_writer.write(data)
        self.__is_actual = False  # Mark as not up-to-date

if __name__ == '__main__':
    reader_reader = TxtReader('my_file.txt')
    writer_writer = TxtWriter('my_file.txt')
    proxy = ProxyTxtRW(reader_reader, writer_writer)

    print("Reading the file:")
    print(proxy.read())  # Read the file
    print(proxy.read())  # Reading again (cached)

    print("\nWriting to the file:")
    proxy.write("This is a new line!")  # Write to the file
    print("Reading the file after writing:")
    print(proxy.read())

