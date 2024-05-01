"""
Este script contiene el codogo del ultimo ejercicio sobre ordenacion con algoritmos. Trata de un algoritmo que se encarga
de analizar si una tabla (interpretando una sublista como tabla) esta o no explorada desde un elemento i inicial, hasta un
elemento j final.
"""

"""
para poder crear listas y tublas genericas, cojo las clases List y tuple de el modulo typing, como he realizado en anteriores
ejercicios de esta practica.
"""
from typing import List, Tuple

"""
Este primer algoritmo, toma como entradas una tabla (lista de enteros) y dos numeros enteros, uno que indica el inicio de los elementos
a analizar, y el fin será el último elemento a analizar. Para ello verifica si cada componente de t[inicio .. fin] está colocada después
de la serie más grande de componentes de la que es el maximo Devuelve un booleano (True o False) en funcion del cumplimiento o no de la condicion.
El algoritmo además contiene otra función que realiza otro proceso a parte para la realizacion del ejercicio (es también un algoritmo). 
Este algoritmo toma como entrada los mismo parametros que la función anterior. Se encarga de encontrar el segmento más grande cuyo valor máximo es 
el primer elemento del segmento. El algoritmo devuelve una tupla con los indices del primer y ultimo elemento del segmento máximo.

"""
def está_explorado(t: List[int], inicio: int, fin: int) -> bool:

    def segmento_maximo(t: List[int], inicio: int, fin: int) -> Tuple[int, int]:

        i = inicio
        maximo = t[i]
        max_index = i
        while i <= fin:
            j = i + 1
            while j <= fin and t[j] >= t[i]:
                if t[j] > maximo:
                    maximo = t[j]
                    max_index = j
                j += 1
            i = j
        return (max_index, fin)

    # Verifica si cada componente está colocado después del segmento máximo
    i = inicio
    while i <= fin:
        max_index, segmento_fin = segmento_maximo(t, i, fin)
        if max_index != i:
            return False
        i = segmento_fin + 1
    return True

# Tabla a usar como ejemplo (es la del enunciado del ejercicio)
t = [5, 7, 12, 6, 18, 13, 9, 10, 16, 21, 19, 8, 20, 3]

# Verifica si la sublista t[2:9] está explorada para mostrar un ejemplo del uso de los algoritmos planteados
inicio = 2
fin = 9
explorado = está_explorado(t, inicio, fin)

if explorado:
    print("La sublista está completamente explorada.")
else:
    print("La sublista no está completamente explorada.")