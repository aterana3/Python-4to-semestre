class Notas:

    def __init__(self, id, n1 = 0, n2 = 0, ex1 = 0, n3 = 0, n4 = 0, ex2 = 0):
        self.id = id
        self.n1 = n1
        self.n2 = n2
        self.ex1 = ex1
        self.n3 = n3
        self.n4 =  n4
        self.ex2 = ex2
    
    def promedio1(self):
        return self.n1 + self.n2 + self.ex1

    def promedio2(self):
        return self.n3 + self.n4 + self.ex2

    def nota_final(self):
        return self.promedio1() + self.promedio2()

    def estado(self):
        return "Aprobado" if self.nota_final() >= 70 else "Reprobado"

    def mostrarDatos(self):
        return f"N1: {self.n1} | N2: {self.n2} | EX1: {self.ex1}| N3: {self.n3} | N4: {self.n4} | EX2: {self.ex2} | NF: {self.nota_final()}| Estado {self.estado()}"