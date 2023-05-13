from abc import ABC, abstractmethod

class FileErrorException(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
        
    def open(self):
        if self.opened:
            raise FileErrorException("File already opened")
        self.opened = True
        
    def close(self):
        if  not self.opened:
            raise FileErrorException("File alread closed")
        self.opened = False
        
    @abstractmethod
    def read(self):
        pass
        
class FileStream(Stream):
    def read(self):
        print("Reading data from a file")
        
class NetworkStream(Stream):
    def read(self):
        print("Readin data from a network")
        
class Memorystream(Stream):
    def read(self):
        print("Readin from memory")
        

stream = Stream()
