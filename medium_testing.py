import time
from medium_red import red_medium, personas
from EstructuraProyecto1 import RedSocial, Camino_naive, Persona, crearVinculo, visualizar_red, ProblemaCamino, Camino, SugerirAmistad, ProblemaSugerirAmistad, calcularAfinidad

# Prueba de camino
ProblemaCamino_medium = ProblemaCamino(red_medium, personas[15], personas[164])
start_time = time.perf_counter()
ans = Camino(ProblemaCamino_medium)
end_time = time.perf_counter()

print("Resultado del camino con A*:")
for paso in ans:
    print(f"{paso[0].nombre} (Coste: {paso[1]})")

print(f"Nodos expandidos usando heurística: {ProblemaCamino_medium.expanded}")
print(f"Tiempo de ejecución (A*): {end_time - start_time:.6f} segundos")
ProblemaCamino_medium.expanded=0

start_time = time.perf_counter()
ans_naive = Camino_naive(ProblemaCamino_medium)
end_time = time.perf_counter()

print("Resultado del camino con ucs:")
for paso in ans_naive:
    print(f"{paso[0].nombre} (Coste: {paso[1]})")

print(f"Nodos expandidos sin usar la heuristica: {ProblemaCamino_medium.expanded}")
print(f"Tiempo de ejecución (UCS): {end_time - start_time:.6f} segundos")

problema_sugerir = ProblemaSugerirAmistad(red_medium, personas[201], personas[177], 0, 1.5)

start_time = time.perf_counter()
ans = SugerirAmistad(problema_sugerir)
end_time = time.perf_counter()

print(personas[201].nombre)
print(ans.nombre)
print("Nodos expandidos para sugerir amistad: ", problema_sugerir.expanded)
print(f"Tiempo de ejecución (Sugerir amistad): {end_time - start_time:.6f} segundos")
