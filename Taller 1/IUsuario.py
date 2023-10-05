from abc import ABC, abstractmethod


class IUsuario(ABC):

    @abstractmethod
    def getNombre(self):
        pass

    @abstractmethod
    def getApellido(self):
        pass

    @abstractmethod
    def mostrarDatos(self):
        pass