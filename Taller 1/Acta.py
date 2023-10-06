from DetActa import DetActa

class Acta:

    def __init__(self, id, curso):
        self.id = id
        self.curso = curso

    def imprimir(self):
        print("Acta de Notas")
        print("------------------------------------")
        print("Curso: " + self.curso.getNombre())
        print("Profesor: " + self.curso.getProfesor().mostrarDatos())
        print("------------------------------------")
        print("Estudiantes: ")
        for estudiante in self.curso.getEstudiantes():
            detActa = DetActa(self.id, estudiante)
            print(detActa.mostrarDatos())