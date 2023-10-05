class Notas:

    def __init__(self, n1 = 0, n2 = 0, ex1 = 0, n3 = 0, n4 = 0, ex2 = 0):
        self.n1 = n1
        self.n2 = n2
        self.ex1 = ex1
        self.n3 = n3
        self.n4 = n4
        self.ex2 = ex2

    @property
    def n1(self):
        return self.__n1
    
    @property
    def n2(self):
        return self.__n2

    @property
    def ex1(self):
        return self.__ex1

    @property
    def n3(self):
        return self.__n3
    
    @property
    def n4(self):
        return self.__n4
    
    @property
    def ex2(self):
        return self.__ex2

    def promedio1(self):
        return (self.__n1 + self.__n2 + self.__ex1)/3

    def promedio2(self):
        return (self.__n3 + self.__n4 + self.__ex2)/3

    def nota_final(self):
        return (self.promedio1() + self.promedio2())

    def estado(self):
        return "Aprobado" if self.nota_final() >= 70 else "Reprobado"

    def mostrarDatos(self):
        return "Nota 1: " + str(self.n1) + "\n" + "Nota 2: " + str(self.n2) + "\n" + "Examen 1: " + str(self.ex1) + "\n" + "Nota 3: " + str(self.n3) + "\n" + "Nota 4: " + str(self.n4) + "\n" + "Examen 2: " + str(self.ex2) + "\n" + "Promedio 1: " + str(self.promedio1()) + "\n" + "Promedio 2: " + str(self.promedio2()) + "\n" + "Nota final: " + str(self.nota_final()) + "\n" + "Estado: " + self.estado() + "\n"
