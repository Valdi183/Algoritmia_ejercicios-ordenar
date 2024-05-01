"""
Este script contiene un ejercicio de algoritmos que se basa en  algoritmos de ordenacion por insercion dicotomica.
La funcion orden_dicotomico_1 ordena la lista en su lugar. Por otro lado la funcion orden_dicotomico_2 devuelve una nueva lista ordenada.
"""

"""
Para realizar el ejercicio, he utilizado las clases List y TypeVar de la libreria typing.
List: Simplemente indica que una variable es una lista de un tipo especifico. Por ejemplo, una lista de enteros: List[int]
Typevar: Sirve para dar definicion a parametros de tipo generico. Po ejemplo, Un parametro "T" que puede ser de varios tipos: T = TypeVar('T', int, float, str)
"""
from typing import List, TypeVar

T = TypeVar('T', int, float, str)

"""
Ordena la lista "t" en su lugar en orden creciente utilizando el algoritmo de insercion dicotomica. Para ello se definen los parametros 
t (una lista de T elementos) que es la que se pretende ordenar con el algoritmo, inicio, que es el indice de inicio de la porcion de la lista
y fin, que es el indice de fin de la porcion de la lista a ordenar (estos mson los datos de entrada del algoritmo). El algoritmo itera sobre 
los elementos de la lista desde inicio + 1, hastafin. Para cada elemento "a" busca su posicion de insercion utilizando el algoritmo de busqueda 
dicotomica. Y finalmente Desplaza los elementos mayores que "a" una posicion a la derecha para hacer espacio para a y asi poder  insertar "a" en 
su lugar. El algoritmo devuelve otra lista nueva con los elementos ya colocados por orden creciente.
"""
def orden_dicotomico_1(t: List[T], inicio: int, fin: int) -> None:
    for i in range(inicio + 1, fin + 1):
        a = t[i]
        # Encuentra la posicion de insercion de "a" usando el algoritmo de busqueda dicotomica
        izquierda, derecha = inicio, i - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if t[medio] < a:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        
        # Desplaza los elementos para hacer espacio para "a"
        for j in range(i, izquierda, -1):
            t[j] = t[j - 1]
        
        # Inserta "a" en su lugar
        t[izquierda] = a

"""
Esta funcion toma los mismo parametros que el algoritmo anterior y el algoritmo los recibe como entrada.
"""
def orden_dicotomico_2(t: List[T], inicio: int, fin: int) -> List[T]:
    resultado = t[inicio:fin + 1].copy()
    orden_dicotomico_1(resultado, 0, fin - inicio)
    return resultado


# Ejemplo de uso para probar ambos algoritmos
t = [-23, 28, 72, 1, 92, -5]
print("Lista original:", t)
orden_dicotomico_1(t, 0, len(t) - 1)
print("Lista ordenada en su lugar:", t)

t2 = [4, 2, 7, 1, 9, 5]
resultado = orden_dicotomico_2(t2, 0, len(t2) - 1)
print("Nueva lista ordenada:", resultado)