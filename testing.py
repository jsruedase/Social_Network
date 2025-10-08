import EstructuraProyecto1 as ep
from EstructuraProyecto1 import RedSocial, Persona, crearVinculo, visualizar_red, ProblemaCamino, Camino, SugerirAmistad, ProblemaSugerirAmistad, calcularAfinidad
import Algorithms.search as search
import network_creation as nc
import random

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
    # ejemplo_base()
    # ejemplo_amistad()
    # ejemplo_small_camino()
    ejemplo_small_amistad()