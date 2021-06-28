from abc import abstractmethod

class GuestBookAbstract(object):
    
    def __init__(self, jsonName):
        self._jsonName = jsonName
    
    @abstractmethod
    def readjson(self, jsonName=self._jsonName):
        pass

    @abstractmethod
    def createjson(self, jsonName=self._jsonName):
        pass

    @abstractmethod
    def deletejson(self, jsonName=self._jsonName):
        pass

    @abstractmethod
    def renamejson(self, newName, jsonName=self._jsonName):
        pass

    @abstractmethod
    def writejson(self, information, jsonName=self._jsonName):
        pass 