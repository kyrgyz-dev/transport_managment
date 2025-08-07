from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self): ...