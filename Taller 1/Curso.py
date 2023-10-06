from Acta import Acta

class Curso:

    def __init__(self, nombre, profesor, estudiantes):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = estudiantes

    def getNombre(self):
        return self.nombre

    def getProfesor(self):
        return self.profesor

    def getEstudiantes(self):
        return self.estudiantes
    
    def generarActa(self):

        acta = Acta(self)
        acta.imprimir()