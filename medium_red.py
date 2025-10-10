import EstructuraProyecto1 as ep
from EstructuraProyecto1 import RedSocial, Persona, crearVinculo, visualizar_red, ProblemaCamino, Camino, SugerirAmistad, ProblemaSugerirAmistad, calcularAfinidad
import csv
import ast

red_medium = RedSocial()
personas = {}  # Diccionario para acceder por ID

# Primera pasada: cargar personas
with open('medium.csv', newline='', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    next(lector)
    for fila in lector:
        try:
            id_persona = int(fila[0])
            nombre = fila[1]
            edad = int(fila[2])
            localidad = fila[3]
            hobbies = ast.literal_eval(fila[4])  # convierte "[1,2,3,4,5]" a lista
            persona = Persona(id_persona, nombre, edad, localidad, hobbies)
            personas[id_persona] = persona
            red_medium.agregar_persona(persona)
        except:
            pass

# Segunda pasada: crear vínculos
with open('medium.csv', newline='', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    next(lector)
    for fila in lector:
        try:
            id_persona = int(fila[0])
            conexiones = ast.literal_eval(fila[5])  # convierte string a lista
            for con_id in conexiones:
                if con_id in personas and id_persona in personas:
                    p1 = personas[id_persona]
                    p2 = personas[con_id]
                    # Evitar duplicar vínculos
                    if p2 not in [v[0] for v in p1.personaCoste]:
                        crearVinculo(p1, p2)
        except:
            break

