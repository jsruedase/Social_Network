import EstructuraProyecto1 as ep
from EstructuraProyecto1 import RedSocial, Persona, crearVinculo, visualizar_red, ProblemaCamino, Camino, SugerirAmistad, ProblemaSugerirAmistad, calcularAfinidad
import Algorithms.search as search
import network_creation as nc
import random
import time
import matplotlib.pyplot as plt

def ejemplo_base():
    red = RedSocial()

    p1 = Persona(1,"Oscar", 25, "Usaquen", [7, 5, 9, 3, 6])
    p2 = Persona(2,"Luis", 27, "Usaquen", [6, 5, 8, 2, 7])
    p3 = Persona(3,"Carlos", 40, "Fontibon", [1, 2, 3, 4, 5])
    p4 = Persona(4,"Marta", 29, "Chapinero", [5, 5, 5, 5, 5])
    p5 = Persona(5,"Elena", 35, "Chapinero", [8, 7, 6, 5, 4])

    for p in [p1, p2, p3, p4, p5]:
        red.agregar_persona(p)

    # Crear vínculos
    crearVinculo(p1, p2)
    crearVinculo(p2, p4)
    crearVinculo(p4, p5)
    crearVinculo(p1, p4)
    # p3 (Carlos) queda aislado

    
    
    problema_camino = ProblemaCamino(red, p1, p3)  # Buscar camino de Oscar a Elena
    ans = Camino(problema_camino)
    
    if problema_camino.existeCamino:
        print("Buscando camino entre Oscar y Carlos:")
        for paso in ans:
            print(f"{paso[0].nombre} (Coste: {paso[1]})")
    else:
        print("No existe camino entre Oscar y Carlos")
        print("Sugerencia de amistad:")
        print(ans.nombre)
    
    
    # Mostrar red
    visualizar_red(red)

def ejemplo_amistad():
    red = RedSocial()

    p1 = Persona(1,"Oscar", 25, "Usaquen", [7, 5, 9, 3, 6])
    p2 = Persona(2,"Luis", 27, "Usaquen", [6, 5, 8, 2, 7])
    p3 = Persona(3,"Carlos", 40, "Fontibon", [1, 2, 3, 4, 5])
    p4 = Persona(4,"Marta", 29, "Chapinero", [5, 5, 5, 5, 5])
    p5 = Persona(5,"Elena", 35, "Chapinero", [8, 7, 6, 5, 4])
    p6 = Persona(6,"Ana", 30, "Usaquen", [7, 6, 8, 4, 5])
    p7 = Persona(7,"Javier", 32, "Usaquen", [6, 5, 7, 3, 4])

    for p in [p1, p2, p3, p4, p5, p6]:
        red.agregar_persona(p)

    # Crear vínculos

    #Bloque amigos 1
    crearVinculo(p1, p2)
    crearVinculo(p2, p4)
    crearVinculo(p4, p5)
    crearVinculo(p1, p4)
    
    #Bloque amigos 2
    crearVinculo(p3, p6)
    crearVinculo(p6, p7)
    crearVinculo(p7, p3)
    
    

    problema_sugerir = ProblemaCamino(red, p1, p3)
    print("Buscando camino entre Oscar y Carlos:")
    ans = Camino(problema_sugerir)
    if problema_sugerir.existeCamino:
        for paso in ans:
            print(f"{paso[0].nombre} (Coste: {paso[1]})")
    else:
        print("No existe camino entre Oscar y Carlos")
        print("Sugerencia de amistad:")
        print(ans.nombre)
        
    # Mostrar red
    visualizar_red(red) 
    crearVinculo(p1,ans)
    visualizar_red(red)


def ejemplo_9pers():
    red = RedSocial()

    p1 = Persona(1, "Ana", 28, "Suba", [7, 6, 5, 3, 8])
    p2 = Persona(2, "Luis", 31, "Suba", [6, 5, 7, 4, 6])
    p3 = Persona(3, "María", 27, "Suba", [8, 6, 5, 5, 7])
    p4 = Persona(4, "Pedro", 40, "Kennedy", [3, 4, 5, 2, 3])
    p5 = Persona(5, "Sofía", 35, "Kennedy", [4, 3, 5, 3, 2])
    p6 = Persona(6, "Carlos", 45, "Chapinero", [6, 7, 8, 5, 4])
    p7 = Persona(7, "Laura", 23, "Chapinero", [7, 8, 6, 5, 5])
    p8 = Persona(8, "Andrés", 29, "Engativá", [5, 6, 4, 5, 5])
    p9 = Persona(9, "Elena", 30, "Engativá", [6, 7, 4, 5, 4])

    for p in [p1,p2,p3,p4,p5,p6,p7,p8,p9]:
        red.agregar_persona(p)

    # Grupo 1 
    crearVinculo(p1, p2)
    crearVinculo(p2, p3)
    crearVinculo(p1, p3)
    # Grupo 2 
    crearVinculo(p4, p5)
    # Grupo 3 
    crearVinculo(p6, p7)
    # Grupo 4 
    crearVinculo(p8, p9)
    problema_sugerir = ProblemaCamino(red, p1, p9)
    print("Buscando camino entre Ana y Elena:")
    ans = Camino(problema_sugerir)
    if problema_sugerir.existeCamino:
        for paso in ans:
            print(f"{paso[0].nombre} (Coste: {paso[1]})")
    else:
        print("No existe camino entre Ana y Elena")
        print("Sugerencia de amistad:")
        print(ans.nombre)
        
    # Mostrar red
    visualizar_red(red) 
    crearVinculo(p1,ans)
    visualizar_red(red)


def ejemplo_10pers():
    red = RedSocial()

    # Grupo A 
    p1 = Persona(1, "Ana", 28, "Usaquén", [8, 7, 6, 5, 7])
    p2 = Persona(2, "Luis", 32, "Chapinero", [6, 5, 8, 7, 6])
    p3 = Persona(3, "Sofía", 27, "Teusaquillo", [7, 6, 7, 6, 8])
    p4 = Persona(4, "Pedro", 30, "Fontibón", [8, 5, 7, 6, 6])
    p5 = Persona(5, "Laura", 29, "Kennedy", [6, 6, 8, 5, 7])

    # Grupo B 
    p6 = Persona(6, "Carlos", 40, "Suba", [5, 6, 7, 8, 7])
    p7 = Persona(7, "María", 35, "Engativá", [6, 7, 5, 8, 7])
    p8 = Persona(8, "Andrés", 33, "Bosa", [7, 8, 6, 6, 8])
    p9 = Persona(9, "Elena", 31, "Puente Aranda", [8, 7, 7, 5, 6])
    p10 = Persona(10, "Javier", 38, "Barrios Unidos", [6, 8, 7, 7, 7])

    for p in [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]:
        red.agregar_persona(p)
    #Conexiones A
    crearVinculo(p1, p2)
    crearVinculo(p2, p3)
    crearVinculo(p3, p4)
    crearVinculo(p4, p5)
    crearVinculo(p5, p1)

    # Conexiones B 
    crearVinculo(p6, p7)
    crearVinculo(p7, p8)
    crearVinculo(p8, p9)
    crearVinculo(p9, p10)
    crearVinculo(p10, p6)
    crearVinculo(p7, p9)
    problema_sugerir = ProblemaCamino(red, p4, p10)
    print("Buscando camino entre Pedro y Javier:")
    ans = Camino(problema_sugerir)
    if problema_sugerir.existeCamino:
        for paso in ans:
            print(f"{paso[0].nombre} (Coste: {paso[1]})")
    else:
        print("No existe camino entre Pedro y Javier")
        print("Sugerencia de amistad:")
        print(ans.nombre)
        
    # Mostrar red
    visualizar_red(red) 
    crearVinculo(p4,ans)
    visualizar_red(red)

def ejemplo_11pers():
    red = RedSocial()

    # Grupo A 
    p1 = Persona(1, "Oscar", 26, "Usaquén", [7, 8, 6, 5, 7])
    p2 = Persona(2, "Luisa", 25, "Chapinero", [6, 7, 8, 6, 7])
    p3 = Persona(3, "Daniel", 24, "Bosa", [7, 6, 7, 8, 6])
    p4 = Persona(4, "Natalia", 27, "Fontibón", [8, 6, 6, 7, 8])
    p5 = Persona(5, "Camilo", 29, "Suba", [7, 5, 7, 6, 8])
    p6 = Persona(6, "Diana", 28, "Engativá", [6, 6, 8, 7, 7])

    # Grupo B 
    p7 = Persona(7, "Felipe", 33, "Kennedy", [8, 7, 7, 6, 8])
    p8 = Persona(8, "Sara", 31, "Teusaquillo", [7, 8, 7, 6, 7])
    p9 = Persona(9, "Mónica", 34, "Barrios Unidos", [6, 8, 7, 7, 6])
    p10 = Persona(10, "Hugo", 32, "Puente Aranda", [8, 6, 6, 7, 7])
    p11 = Persona(11, "Claudia", 29, "Antonio Nariño", [7, 7, 6, 8, 7])

    for p in [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]:
        red.agregar_persona(p)

     #Conexiones A
    crearVinculo(p1,p2)
    crearVinculo(p2,p3)
    crearVinculo(p3,p4)
    crearVinculo(p4,p5)
    crearVinculo(p5,p6)
    crearVinculo(p6,p1)
    crearVinculo(p2,p5)
     #Conexiones B
    crearVinculo(p7,p8)
    crearVinculo(p8,p9)
    crearVinculo(p9,p10)
    crearVinculo(p10,p11)
    crearVinculo(p11,p7)
    crearVinculo(p8,p10)
    problema_sugerir = ProblemaCamino(red, p6, p7)
    print("Buscando camino entre Diana y Felipe:")
    ans = Camino(problema_sugerir)
    if problema_sugerir.existeCamino:
        for paso in ans:
            print(f"{paso[0].nombre} (Coste: {paso[1]})")
    else:
        print("No existe camino entre Diana y Felipe")
        print("Sugerencia de amistad:")
        print(ans.nombre)
        
    # Mostrar red
    visualizar_red(red) 
    crearVinculo(p6,ans)
    visualizar_red(red)




    
def ejemplo_small_camino():
    red = ep.RedSocial()
    nombre_archivo = 'Data/small.csv'
    red = nc.crearRed(nombre_archivo)
    
    p1 = red.obtener_persona_por_id(random.randint(1,99)) 
    p2 = red.obtener_persona_por_id(random.randint(1,99))
    p3 = red.obtener_persona_por_id(100)
    
    print(f"Buscando camino entre {p1.nombre} y {p3.nombre}:")
    
    problema_camino = ProblemaCamino(red, p1, p3) 
    ans = Camino(problema_camino)
    if problema_camino.existeCamino:
        for paso in ans:
            print(f"{paso[0].nombre} (Coste: {paso[1]})")
    else:
        print(f"No existe camino entre {p1.nombre} y {p3.nombre}")
        print("Sugerencia de amistad:")
        print(ans.nombre)

def ejemplo_small_amistad():
    red = ep.RedSocial()
    nombre_archivo = 'Data/small.csv'
    red = nc.crearRed(nombre_archivo)
    
    p1 = red.obtener_persona_por_id(47) 
    p2 = red.obtener_persona_por_id(100)
    
    print(f"Buscando camino entre {p1.nombre} y {p2.nombre}:")
    
    #para 0.5, 1, 2 cambian los resultados
    problema_sugerir = ProblemaSugerirAmistad(red, p1, p2, 0, 0.5)
    ans = SugerirAmistad(problema_sugerir)
    
    print(ans.nombre)


if __name__ == "__main__":
    #ejemplo_base()
    #ejemplo_amistad()
    # ejemplo_small_camino()
    #ejemplo_small_amistad()
    #ejemplo_9pers()
    #ejemplo_10pers()
    ejemplo_11pers()
