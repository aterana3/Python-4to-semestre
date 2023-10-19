from Profesor import Profesor
from Estudiante import Estudiante
from Notas import Notas
from Curso import Curso
import json 
# profesor = Profesor(1, "Daniel Alexander", " Vera Paredes")

# nota_1 = Notas(15, 15, 20, 10, 10, 15)
# estudiante_1 = Estudiante(1, "Juan", "Perez", nota_1)

# nota_2 = Notas(15, 15, 20, 10, 10, 15)
# estudiante_2 = Estudiante(2, "Anthony", "Terán", nota_2)

# estudiantes = {estudiante_1, estudiante_2}

# curso = Curso("Software A1", profesor, estudiantes)

# curso.generarActa()

acta = {
    "profesor": {
        "nombre": "Daniel Alexander",
        "apellido": "Vera Paredes"
    },
    "nota_1": {
        "nota": "15, 15, 20, 10, 10, 15",
        "estudiante": {
            "nombre": "Juan",
            "apellido": "Perez"
        }
    },
    "curso": "software A1"
}
nombre_archivo = "acta.json"
with open(nombre_archivo, 'w') as archivo: 
    json.dump(acta, archivo, indent = 4)

print(f"Se  ha creado el archivo {nombre_archivo}")


