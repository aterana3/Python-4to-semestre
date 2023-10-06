from DetActa import DetActa

class Acta:

    def __init__(self, curso):
        self.curso = curso

    def imprimir(self):
        print("Acta de Notas")
        print("------------------------------------")
        print("Curso: " + self.curso.getNombre())
        print("Profesor: " + self.curso.getProfesor().mostrarDatos())
        print("------------------------------------")
        print("Estudiantes: ")
        for estudiante in self.curso.getEstudiantes():
            detActa = DetActa(estudiante)
            print(detActa.mostrarDatos())