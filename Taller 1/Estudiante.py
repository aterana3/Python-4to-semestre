from IUsuario import IUsuario

class Estudiante(IUsuario):

    def __init__(self, id, nombre, apellido, notas):
        super().__init__(id, nombre, apellido)
        self.notas = notas

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido
    
    def getNotas(self):
        return self.notas

    def mostrarDatos(self):
        return "Nombre: " + self.nombre + " " + self.apellido + " |" + self.notas.mostrarDatos() 