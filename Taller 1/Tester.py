from Profesor import Profesor
from Estudiante import Estudiante
from Notas import Notas
from Curso import Curso

profesor = Profesor("Daniel Alexander", " Vera Paredes")

nota_1 = Notas(15, 15, 20, 10, 10, 15)
estudiante_1 = Estudiante("Juan", "Perez", nota_1)

nota_2 = Notas(15, 15, 20, 10, 10, 15)
estudiante_2 = Estudiante("Anthony", "Terán", nota_2)

estudiantes = {estudiante_1, estudiante_2}

curso = Curso("Software A1", profesor, estudiantes)

curso.generarActa()