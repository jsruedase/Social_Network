from typing import List
import math
import random
import matplotlib.pyplot as plt
import networkx as nx


class Persona:
    def __init__(self, nombre: str, edad: int, localidad: str, afinidadHobbies: List[int]):
        self.nombre=nombre
        self.edad=edad
        self.localidad=localidad
        self.afinidadHobbies=afinidadHobbies
        self.personaCoste: List[tuple[Persona, int]] = [] ##lista personas para añadir los vinculos



def crearVinculo(p1: Persona, p2: Persona) -> int: 
    """
        Funcion para crear vinculos expresamente usando la afinidad y un entero mayor que 1
        
    
    """
    afinidadPersonas=calcularAfinidad(p1,p2)
    n=random.randint(2, 10)
    coste=afinidadPersonas*n
    p1.personaCoste.append((p2, coste))
    p2.personaCoste.append((p1, coste))



def calcularAfinidad(p1: Persona, p2: Persona) -> int:
    """
    Funcion para calcular afinidad entre dos personas usando sus atributos
    Edad: entre mas cercana mas afinidad
    Localidad: si es la misma extra, aun no con distancia
    Hobbies: Distancia euclidea en R^5 
    """

    # Pesos de cada atributo AJUSTAR
    PESO_EDAD = 0.4
    PESO_LOCALIDAD = 0.2
    PESO_HOBBIES = 0.4

    # Edad
    diferenciaEdad = abs(p1.edad - p2.edad)/100 #100 para que esté entre 0 y 1
    puntajeEdad = 1 - min(1, diferenciaEdad)  

    #  Localidad 
    puntajeLocalidad = 1 if p1.localidad == p2.localidad else 0

    #  Hobbies 
    # Usamos distancia euclídea normalizada
    diferenciaHobbies = math.sqrt(sum((a - b) ** 2 for a, b in zip(p1.afinidadHobbies, p2.afinidadHobbies)))
    maxDist = math.sqrt(5 * (9 ** 2)) 
    puntajeHobbies=1-(diferenciaHobbies / maxDist)

    # Afinidad Final
    afinidad = (PESO_EDAD*puntajeEdad  +PESO_LOCALIDAD*puntajeLocalidad +  PESO_HOBBIES*puntajeHobbies)

    # Escalamos a 0 a 100
    return int(round(afinidad * 100))



class RedSocial:
    def __init__(self):
        self.personas = [] #Listado global de las personas en la red Social
        
 
    def agregar_persona(self, persona):
        self.personas.append(persona)



class ProblemaCamino:
    """
    Clase para manejar el problema de encontrar camino entre dos personas
    En caso de que no se encuentre se sigue al problema de sugerir amistad
    """

    def __init__(self,red: RedSocial, estadoInicial: Persona, estadoObjetivo: Persona):
        self.red=red #Conjunto de personas donde estamos haciendo la busqueda, se presupone que persona inicial y objetivo se encuentran ya
        self.estadoInicial=estadoInicial
        self.estadoObjetivo=estadoObjetivo
        self.existeCamino=True #Suponemos verdero inicialmente 

    def isGoalState(self, persona: Persona) -> bool:
        return persona == self.estadoObjetivo
    
    def sucesores(self, persona:Persona)->List[tuple[Persona, int]]:
        return persona.personaCoste
    

class ProblemaSugerirAmistad:
    """
    Clase encargada de manejar lo relativo al problema de sugerir amistad
    """

    def __init__(self, red:RedSocial, estadoInicial: Persona, estadoObjetivo: Persona ):
        self.red=red
        self.estadoInicial=estadoInicial
        self.estadoObjetivo=estadoObjetivo
    
    """
    Para sugerir amistad se simula la creacion de un vinculo entre todas las person
    y se repite el proceso de busqueda de mejor camino
    se da por sugerencia aquella que se usó para el camino??????
    """

##Como reconstruir el camino???  Conjunto de acciones, como se hace??? se guarda como [persona 1-> persona 2]+ [persona2->persona3]?? esto donde se guarda


"""

    IMPORTANTEEEEEEEEEEEEEEEE
        -Como manejar la sugerencia de amistad
        -Reconstruccion de camino acciones para llegar
        -Ajustar pesos
        -Definir listado de hobbies
        -Crear ejemplos base
        -Crear ejemplos random
        -Complejidad?? Tiempo memoria
        -BFS, DFS, UCS, A*
        -Ajustar visualizador para ver mejor los grafos
        -
        -
        -
        -





"""
    


def visualizar_red(red: RedSocial):
    G = nx.Graph()

    # Añadir nodos
    for persona in red.personas:
        G.add_node(persona.nombre, label=persona.localidad)

    # Añadir aristas con pesos
    for persona in red.personas:
        for vecino, coste in persona.personaCoste:
            if not G.has_edge(persona.nombre, vecino.nombre):
                G.add_edge(persona.nombre, vecino.nombre, weight=coste)

    # Layout espacioso
    pos = nx.spring_layout(G, seed=42, k=30)

    plt.figure(figsize=(8,6))

    # Nodos
    nx.draw_networkx_nodes(G, pos, node_size=1800, node_color="lightblue", edgecolors="black")

    # Etiquetas de nodos
    nx.draw_networkx_labels(G, pos, font_size=12, font_color="black", font_weight="bold")

    # Aristas
    nx.draw_networkx_edges(G, pos, width=2.5, edge_color="darkgray")

    # Etiquetas de aristas (coste)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color="red")

    plt.title("Red Social - Personas y Afinidades", fontsize=14)
    plt.axis("off")
    plt.show()


# ---------------------------
# Ejemplo de uso
# ---------------------------

red = RedSocial()

p1 = Persona("Oscar", 25, "Usaquen", [7, 5, 9, 3, 6])
p2 = Persona("Luis", 27, "Usaquen", [6, 5, 8, 2, 7])
p3 = Persona("Carlos", 40, "Fontibon", [1, 2, 3, 4, 5])
p4 = Persona("Marta", 29, "Chapinero", [5, 5, 5, 5, 5])
p5 = Persona("Elena", 35, "Chapinero", [8, 7, 6, 5, 4])

for p in [p1, p2, p3, p4, p5]:
    red.agregar_persona(p)

# Crear vínculos
crearVinculo(p1, p2)
crearVinculo(p2, p4)
crearVinculo(p4, p5)
crearVinculo(p1, p5)
# p3 (Carlos) queda aislado

# Mostrar red
visualizar_red(red)