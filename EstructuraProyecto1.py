from typing import List
import math
import random
import matplotlib.pyplot as plt
import networkx as nx
from Algorithms import search
import numpy as np


class Persona:
    def __init__(self, id: int, nombre: str, edad: int, localidad: str, afinidadHobbies: List[int]):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.localidad = localidad
        self.afinidadHobbies = afinidadHobbies
        self.personaCoste: List[tuple[Persona, int]] = [] ##lista personas para añadir los vinculos

    def obtener_vecino_con_coste(self, cost: int) -> tuple['Persona', int]:
        for vecino, coste in self.personaCoste:
            if coste == cost:
                return (vecino, coste)
        return None


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

def road_heuristic(state, problem):
    """
    
    Esta heurística es admisible ya que nunca sobreestima el costo real hacia la solución
    lo que hace es calcular la afinidad máxima posible, no mínima distancia y dado el 
    contexto en el que se esta trabajando, esto permite que la solución sea optima y eficiente
    """
    return calcularAfinidad(state, problem.estadoObjetivo)

class RedSocial:
    def __init__(self):
        self.personas = {} #Listado global de las personas en la red Social
    
    def agregar_persona(self, persona):
        self.personas[persona.id] = persona
    
    def obtener_persona_por_id(self, id):
        return self.personas.get(id, None)



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
        self.expanded = 0

    def getStartState(self) -> Persona:
        return self.estadoInicial
    
    def isGoalState(self, persona: Persona) -> bool:
        return persona == self.estadoObjetivo

    def getSuccessors(self, persona: Persona) -> List[tuple[Persona, int]]:
        self.expanded += 1
        return persona.personaCoste

    def getCostOfActions(self, actions: List[tuple[Persona, int]]) -> int:
        totalCost = 0
        for action in actions:
            totalCost += action[1]
        return totalCost

        
        
    
class ProblemaSugerirAmistad:
    """
    Clase encargada de manejar lo relativo al problema de sugerir amistad
    """

    def __init__(self, red:RedSocial, estadoInicial: Persona, estadoObjetivo: Persona, afinidad_minima: int=0, dificultad_relacion: int=1):
        self.red=red
        self.estadoInicial=estadoInicial
        self.estadoObjetivo = estadoObjetivo
        self.afinidad_minima=afinidad_minima
        self.dificultad_relacion = dificultad_relacion
    
    def getStartState(self) -> Persona:
        return self.estadoObjetivo
    
    def isGoalState(self, persona: Persona) -> bool:
        
        if persona == self.estadoObjetivo:
            return False

        #and calcularAfinidad(persona, self.estadoInicial) >  self.dificultad_relacion * calcularAfinidad(self.estadoInicial, self.estadoObjetivo)
        if calcularAfinidad(persona, self.estadoInicial) > self.afinidad_minima and calcularAfinidad(persona, self.estadoInicial) >  self.dificultad_relacion * calcularAfinidad(self.estadoInicial, self.estadoObjetivo):
            return True

        return False
        
    def getSuccessors(self, persona: Persona) -> List[tuple[Persona, int]]:
        return persona.personaCoste
    
    def getCostOfActions(self, actions: List[tuple[Persona, int]]) -> int:
        totalCost = 0
        for action in actions:
            totalCost += action[1]
        return totalCost


def SugerirAmistad(P: ProblemaSugerirAmistad):
    """
    Funcion para sugerir amistad entre dos personas. 
    """
    sugerencia = search.breadthFirstSearch(P)
    print(sugerencia)
    if len(sugerencia) == 0:
        ans= P.estadoObjetivo
    else:
        ans= sugerencia[-1][0].obtener_vecino_con_coste(sugerencia[-1][1])[0]
    
    return ans
        
def Camino(P: ProblemaCamino):
    """
    Funcion para determinar si existe camino entre dos personas
    """
    camino = search.aStarSearch(P, heuristic = road_heuristic)

    if len(camino) == 0:
        P.existeCamino=False
        P2 = ProblemaSugerirAmistad(P.red, P.estadoInicial, P.estadoObjetivo, 0)
        ans = SugerirAmistad(P2)
        return ans
    else:
        return camino
    
# ---------------------------
# Visualización de la red social
# ---------------------------

def visualizar_red(red: RedSocial):

    G = nx.Graph()

    # nodos
    for persona in red.personas.values():
        G.add_node(persona.nombre, label=persona.localidad)

    # pesos
    for persona in red.personas.values():
        for vecino, coste in persona.personaCoste:
            if not G.has_edge(persona.nombre, vecino.nombre):
                G.add_edge(persona.nombre, vecino.nombre, weight=coste)

    if len(G) == 0:
        print("No hay nodos para mostrar.")
        return

    componentes = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    n_comp = len(componentes)
    max_nodos = max(len(c) for c in componentes)

    posiciones = {}
    base_offset = 6.0
    angulo = 0

    for i, comp in enumerate(componentes):
        n = len(comp)
        factor = 0.5 + 1.8 * (n / max_nodos)
        escala = 2.0 * factor
        k_val = (1.0 / math.sqrt(n)) * factor * 0.9

        pos_local = nx.spring_layout(comp, seed=42, k=k_val, iterations=150, scale=escala)

        offset_x = (base_offset * (1.5 if n > max_nodos * 0.7 else 1.0)) * np.cos(angulo)
        offset_y = (base_offset * (1.5 if n > max_nodos * 0.7 else 1.0)) * np.sin(angulo)
        angulo += 2 * np.pi / n_comp

        for nodo, (x, y) in pos_local.items():
            posiciones[nodo] = np.array([x + offset_x, y + offset_y])

    fig = plt.figure(figsize=(16, 9))
    mng = plt.get_current_fig_manager()
    try:
        mng.window.state('zoomed')
    except:
        try:
            mng.resize(*mng.window.maxsize())
        except:
            pass

    nx.draw_networkx_nodes(G, posiciones, node_size=1800, node_color="lightblue", edgecolors="black")
    nx.draw_networkx_labels(G, posiciones, font_size=12, font_color="black", font_weight="bold")
    nx.draw_networkx_edges(G, posiciones, width=2.3, edge_color="gray", alpha=0.7, connectionstyle="arc3,rad=0.07")

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, posiciones, edge_labels=edge_labels, font_size=10, font_color="red")

    plt.title("Red Social - Personas y Afinidades", fontsize=14, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.show()









# ---------------------------
# Ejemplo de uso
# ---------------------------

if __name__ == "__main__":
    red1 = RedSocial()

    nombres = [
        ("Ana", 22, "Usaquén"),
        ("Luis", 24, "Usaquén"),
        ("Marta", 25, "Chapinero"),
        ("Julián", 23, "Chapinero"),
        ("Sofía", 21, "Suba"),
        ("Andrés", 27, "Usme"),
        ("Camila", 26, "Suba"),
        ("Carlos", 24, "Usme"),
        ("Elena", 25, "Usaquén")
    ]

    for i, (n, e, l) in enumerate(nombres, start=1):
        red1.agregar_persona(Persona(i, n, e, l, [random.randint(1,10) for _ in range(5)]))

    # Crear vínculos
    crearVinculo(red1.personas[1], red1.personas[2])
    crearVinculo(red1.personas[2], red1.personas[3])
    crearVinculo(red1.personas[3], red1.personas[4])
    crearVinculo(red1.personas[4], red1.personas[5])
    crearVinculo(red1.personas[1], red1.personas[6])
    crearVinculo(red1.personas[5], red1.personas[7])
    crearVinculo(red1.personas[8], red1.personas[9])
    crearVinculo(red1.personas[7], red1.personas[8])
    crearVinculo(red1.personas[2], red1.personas[9])

    visualizar_red(red1)

    
