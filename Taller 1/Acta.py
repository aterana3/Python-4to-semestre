from DetActa import DetActa

class Acta:

    _secuencia = 0

    def __init__(self, curso):
        Acta._secuencia += 1
        self.id = Acta._secuencia
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