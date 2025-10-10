from small_red import red_small , personas 
from EstructuraProyecto1 import RedSocial, Camino_naive, Persona, crearVinculo, visualizar_red, ProblemaCamino, Camino, SugerirAmistad, ProblemaSugerirAmistad, calcularAfinidad
import time

# Prueba de camino
ProblemaCamino_small = ProblemaCamino(red_small, personas[15], personas[64])
start_time = time.perf_counter()
ans = Camino(ProblemaCamino_small)
end_time = time.perf_counter()

print("Resultado del camino con A*:")
for paso in ans:
    print(f"{paso[0].nombre} (Coste: {paso[1]})")

print(f"Nodos expandidos usando heurística: {ProblemaCamino_small.expanded}")
print(f"Tiempo de ejecución (A*): {end_time - start_time:.6f} segundos")


start_time = time.perf_counter()
ans_naive = Camino_naive(ProblemaCamino_small)
end_time = time.perf_counter()

print("Resultado del camino con ucs:")
for paso in ans_naive:
    print(f"{paso[0].nombre} (Coste: {paso[1]})")

print(f"Nodos expandidos sin usar la heuristica: {ProblemaCamino_small.expanded}")
print(f"Tiempo de ejecución (UCS): {end_time - start_time:.6f} segundos")

problema_sugerir = ProblemaSugerirAmistad(red_small, personas[100], personas[34], 0, 1)

start_time = time.perf_counter()
ans = SugerirAmistad(problema_sugerir)
end_time = time.perf_counter()

print(personas[100].nombre)
print(ans.nombre)
print("Nodos expandidos para sugerir amistad: ", problema_sugerir.expanded)
print(f"Tiempo de ejecución (Sugerir amistad): {end_time - start_time:.6f} segundos")
