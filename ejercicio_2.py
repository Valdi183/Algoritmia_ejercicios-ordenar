"""
Este script contiene la solución del segundo ejercicio. Aqui se propone un algortitmo que realiza una ordenacion topologica
de una serie de tareas cumpliendo tambien con las restricciones propuestas en el enunciado. Para este algoritmo se ha utilizado
un metodo de busqueda llamado DFS (metodo de busqueda en profundidad)
"""
"""
Se utiliza la clase List de la libreria typing para de forma simiar al ejercicio anterior, indicar una variable de tipo lista
con n elementos de cualquir tipo (en este caso los elementos seran las restricciones representadas como tuplas de elementos (i , j)
"""
from typing import List

"""
El algoritmo representado por esta función, toma como datos de entrada, una lista de tuplas, que representan las restricciones y un
numero natural (n), que representa el numero de tareas. Se construye un grafo dirigido donde los nodos representan las tareas y las 
aristas representan las restricciones de prioridad. Se calculan los grados de entrada de cada nodo. Posteriormente se realiza un recorrido DFS para 
obtener una ordenación topológica de las tareas. Si todas las tareas pueden ser ordenadas, se devuelve la ordenación topológica. 
En caso contrario, se devuelve una lista vacía para indicar que no es posible realizar una ordenación topológica debido a la presencia de ciclos.
El algoritmo devuelve esa lista, o bien de las n tareas ordenadas, o bien vacia.
"""
def ordenacion_topologica(n: int, restricciones: List[tuple]) -> List[int]:
    grafo = [[] for _ in range(n)]
    grados_entrada = [0] * n

    # Construye el grafo y calcular los grados de entrada
    for u, v in restricciones:
        grafo[u - 1].append(v - 1)
        grados_entrada[v - 1] += 1

    # Función DFS para ordenación topológica
    def dfs(u):
        visitado[u] = True
        for v in grafo[u]:
            if not visitado[v]:
                dfs(v)
        orden.insert(0, u)

    # Inicializa variables
    visitado = [False] * n
    orden = []

    # Inicia el DFS desde los nodos con grado de entrada cero
    for i in range(n):
        if grados_entrada[i] == 0 and not visitado[i]:
            dfs(i)

    # Verifica si existe una ordenación topológica
    if len(orden) != n:
        return []  # No hay ordenación topológica

    return [x + 1 for x in orden]  # Ajusta los índices (1-indexed)

# Ejemplo de uso
n = 5
restricciones = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
orden = ordenacion_topologica(n, restricciones)
if orden:
    print("Ordenación topológica de las tareas:", orden)
else:
    print("No es posible realizar una ordenación topológica debido a ciclos.")