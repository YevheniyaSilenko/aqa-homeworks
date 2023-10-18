from abc import ABC, abstractmethod


class Read(ABC):

    @abstractmethod
    def read(self):
        pass
