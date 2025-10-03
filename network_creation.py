import csv
import ast
import EstructuraProyecto1 as ep

def crearRed(nombre_archivo):
    red = ep.RedSocial()

    #Crear los nodos
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo) 

        for fila in lector_csv:
            persona = ep.Persona(
                id=int(fila['id']),
                nombre=fila['nombre_apellido'],
                edad=int(fila['edad']),
                localidad=fila['localidad'],
                afinidadHobbies=ast.literal_eval(fila['lista_numeros']),
            )
            red.agregar_persona(persona)
    
    #Crear los vinculos
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo) 

        for fila in lector_csv:
            persona_actual = red.obtener_persona_por_id(int(fila['id']))
            conexiones = ast.literal_eval(fila['conexiones'])
            for conexion in conexiones:
                persona_conectada = red.obtener_persona_por_id(conexion)
                ep.crearVinculo(persona_actual, persona_conectada)
    
    return red


if __name__ == "__main__":
    red = ep.RedSocial()
    nombre_archivo = 'Data/medium.csv'
    red = crearRed(nombre_archivo)
    for persona in red.personas.values():
        print(f"Persona: {persona.nombre}, Conexiones y Costes: {[(red.obtener_persona_por_id(i.id).id, c) for i, c in persona.personaCoste]}")

    ep.visualizar_red(red)
            