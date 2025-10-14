# Social_Network
## 1. Introducción

Las redes sociales son un ejemplo natural de estructuras de grafos, donde cada persona puede modelarse como un nodo y las relaciones de amistad como aristas. Estas estructuras permiten estudiar fenómenos de conexión, propagación de información, recomendación de contactos y análisis de comunidades.

La inteligencia artificial, en particular los algoritmos de búsqueda, ofrece herramientas para resolver problemas de navegación y exploración en estos grafos. Implementar algoritmos clásicos como **Búsqueda en Anchura (BFS)**, **Búsqueda en Profundidad (DFS)**, **Búsqueda de Costo Uniforme (UCS)** y **A*** sobre una red social sintética brinda un escenario pedagógico y práctico para comprender el funcionamiento, ventajas y limitaciones de cada método.

El presente proyecto propone modelar una red social de la ciudad de Bogotá, incorporando atributos personales y un nivel de relación que sirva como peso en las conexiones. Con esta representación, se busca resolver problemas de búsqueda de rutas sociales, sugerencia de amigos y emparejamiento, utilizando algoritmos de IA.

Los principales objetivos son:

- Analizar cómo distintos algoritmos exploran grafos sociales.
- Comparar búsquedas no informadas (BFS, DFS) con búsquedas informadas (UCS, A*).
- Modelar fenómenos reales como:
    - Encontrar conexiones sociales indirectas.
    - Sugerir amistades probables.
    - Proponer emparejamientos ideales según afinidades.

La motivación práctica es que este tipo de modelos son la base de sistemas de recomendación modernos en redes sociales, plataformas de citas y motores de networking profesional.

---

## 2. Definición del problema

Se plantea una red social donde:

- Cada persona es un nodo con atributos:
    - Edad.
    - Localidad de Bogotá donde vive.
    - Hobbies representados en un diccionario con intensidad de interés.
- Cada arista representa una amistad y está asociada a un **nivel de relación**, que indica la fuerza o cercanía de la amistad.

El grafo es no dirigido. El costo de moverse entre dos personas está determinado por la afinidad entre las características que comparten, que se calcula con una función en la que entra como parámetro los hobbies y el gusto por estos. Entre más compartan hobbies y más cerca vivan, mayor será la relación de amistad y por ende menor el coste de pasar de un nodo a otro. Se hace un promedio ponderado donde la edad vale el 40%, la localidad el 20% y la afinidad por los hobbies otro 40%. Sin embargo esto no siempre ocurre fielmente a la realidad y es por esto que este valor será multiplicado por un entero k mayor o igual que 1 (y acotado), es decir:


---

## 3. Objetivos

1. **Búsqueda de un camino:**
    - Dada una persona origen y una persona objetivo, determinar si existe una ruta de amistad a través de amigos de amigos.
    - Si no existe, sugerir la persona más fácil de conectar (según atributos y afinidad) para que la ruta se establezca y que esta tenga el menor costo posible.
2. **Sugerencia de nuevas amistades:**
    - Dada una persona, identificar cuál sería el candidato más probable a convertirse en amigo, entre los amigos de sus amigos, usando la afinidad de atributos.

---

## 4. Definición de estados

Como queremos resolver principalmente dos objetivos, necesitaremos dos clases de problemas para diferenciar la definición de estados:

Para ambos problemas el estado inicial será la persona origen dada por parámetro a la cual se le quiere hallar una persona objetivo u otro candidato posible a ser amigo. El estado actual será entonces la persona en el n-ésimo paso durante la búsqueda.

Sin embargo, si no hay un camino que una dos nodos se deberá tener otra consideración: en ese caso se debe identificar cuál sería la persona más conveniente de conectar directamente, es decir, aquella que pertenezca al mismo componente conexo del objetivo y que además tenga el menor costo de relación (o la mayor afinidad) con la persona origen. De este modo, aunque no exista ruta en el grafo actual, se sugiere un nuevo estado que represente la posibilidad de añadir una arista hacia ese candidato y así crear la ruta faltante.

---

## 5. Definición de función sucesora

Haciendo la misma aclaración de antes, vemos que para ambos problemas será común que la función sucesora sea la lista de amigos a los que está conectado el nodo actual y el costo de la relación (inverso al nivel de relación).

En caso que no exista un camino entre dos personas, se debe definir la misma función sucesora pero a partir de la persona a hallar y tener consideraciones extra: en este escenario se calcula el conjunto de nodos que podrían servir como puente entre la persona origen y la persona objetivo. Para cada candidato se evalúa el costo de crear una nueva conexión directa con la persona origen y se incluye como sucesor virtual. De esta manera, la función sucesora no se limita únicamente a los vecinos actuales, sino también a las conexiones potenciales que permitirían enlazar componentes desconectados.

---

## 6. Prueba de objetivo

En ambos casos la prueba de objetivo será si la persona actual es la persona a buscar. Si se recorren todos los posibles caminos y no se halla la persona, se debe tomar otra consideración extra: en este caso el algoritmo debe reportar que no existe ruta en el grafo actual, y complementar el resultado con la recomendación de la persona más adecuada a conectar (según el menor costo de relación y mayor afinidad), para que en un futuro sí sea posible alcanzar al objetivo.

En el objetivo de la sugerencia de amistad, se debe verificar si ya se visitaron todos los amigos de los amigos de la persona inicial. Una vez cubiertos, se debe escoger como resultado final el candidato con mayor probabilidad de amistad, es decir, aquel que maximice la combinación entre número de amigos en común y similitud en atributos personales.

---

## 7. Resultados

Se medirán en ambos problemas el número de nodos expandidos, los costos de las rutas encontradas (si hay) y el tiempo de ejecución, variando el número de personas del grafo y viendo qué sucede si el grafo es denso o disperso para evaluar la eficiencia de los algoritmos implementados.

Red Pequeña:

| Algoritmo | Camino encontrado                                                                | Nodos expandidos | Tiempo de ejecución (s) |
| --------- | -------------------------------------------------------------------------------- | ---------------- | ----------------------- |
| **A***    | Alejandro Vargas → Elena Beltrán → Lucas Pineda → Matías Moreno → Adrián Cabrera | 27               | 0.001303                |
| **UCS**   | Alejandro Vargas → Elena Beltrán → Lucas Pineda → Matías Moreno → Adrián Cabrera | 30               | 0.000300                |

Sugerencia de amistad:

Nodo inicial: Juan Rueda
Sugerencia obtenida: Sebastián Díaz
Nodos expandidos: 11
Tiempo de ejecución: 0.000524 s

Red Mediana:

| Algoritmo | Camino encontrado                                                     | Nodos expandidos | Tiempo de ejecución (s) |
| --------- | --------------------------------------------------------------------- | ---------------- | ----------------------- |
| **A***    | Sebastián Castro → Leonardo Rubio → Diego Castillo → Joaquín Castillo | 98               | 0.002395                |
| **UCS**   | Sebastián Castro → Leonardo Rubio → Diego Castillo → Joaquín Castillo | 109              | 0.001174                |

Sugerencia de amistad:
Nodo inicial: Andrés Duque
Sugerencia obtenida: Alejandro Flores
Nodos expandidos: 28
Tiempo de ejecución: 0.001504 s

En cuanto al tiempo de ejecución, los resultados son coherentes con el comportamiento esperado de ambos algoritmos.

En la red pequeña, UCS fue ligeramente más rápido (0.0003 s vs. 0.0013 s), lo cual es razonable, ya que el cálculo de la heurística en A* puede representar una carga adicional cuando el tamaño del problema es reducido.

En la red mediana, A* también presentó un mayor tiempo de ejecución (0.0024 s vs. 0.0011 s), lo que concuerda con su naturaleza: este algoritmo realiza evaluaciones heurísticas adicionales que, aunque aumentan el tiempo, permiten expandir menos nodos y encontrar el camino óptimo de manera más eficiente en términos de exploración.

El módulo de SugerirAmistad busca candidatos de conexión basándose en medidas de afinidad dentro de la red.
En la red pequeña, el sistema exploró 11 nodos y sugirió conectar a Juan Rueda con Sebastián Díaz.
En la red mediana, exploró 28 nodos y sugirió a Alejandro Flores como mejor conexión para Andrés Duque.
En ambos casos, el tiempo de ejecución fue muy bajo (del orden de milisegundos), lo que demuestra que el algoritmo es eficiente y escalable incluso con un crecimiento considerable del tamaño de la red.

---
## 8. Conclusiones

1) A* y UCS encuentran caminos óptimos, pero A* expande menos nodos gracias al uso de una heurística informada.
2) La heurística utilizada es efectiva y consistente, guiando la búsqueda hacia las soluciones óptimas.
3) El algoritmo de sugerencia de amistad funciona correctamente, con tiempos de ejecución bajos y una exploración controlada, lo cual es deseable en sistemas de recomendación.

---
## 9. Ejemplos 9, 10 y 11 personas
### Ejemplo 9 personas
**Antes:** 
<img width="1872" height="930" alt="image" src="https://github.com/user-attachments/assets/7b80382e-e22a-4f0c-8c15-661ff33d54c2" />

**Después:** 
<img width="1744" height="885" alt="image" src="https://github.com/user-attachments/assets/c65cba5e-9bfc-4d6a-a1e9-3953712dcfec" />

### Ejemplos 10 personas
**Antes:** 
<img width="1855" height="876" alt="image" src="https://github.com/user-attachments/assets/2a01ca71-5994-4b88-b38b-e679f906a8c2" />

**Después:** 
<img width="1823" height="876" alt="image" src="https://github.com/user-attachments/assets/7a071107-32b5-4e57-bba5-fae1fcc7ff86" />

### Ejemplos 11 personas
**Antes:**
<img width="1822" height="881" alt="image" src="https://github.com/user-attachments/assets/b308344a-cc4e-4120-b7f3-30b1ea12aeef" />

**Después:** 
<img width="1832" height="920" alt="image" src="https://github.com/user-attachments/assets/ad63ffd5-d74b-4cda-9f31-5f8ece67f0eb" />
