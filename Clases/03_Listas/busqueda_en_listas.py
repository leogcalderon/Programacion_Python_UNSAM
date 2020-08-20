import math

def buscar_u_elemento(lista,elemento):
    '''
    Devuelve la posición de la última aparición
    de un elemento en la lista
    (o -1 si el elemento no pertenece a la lista).
    '''
    index = -1
    for i, e in enumerate(lista):
        if lista[-(i+1)] == elemento:
            index = len(lista) - i - 1
            break
    return index


def buscar_n_elemento(lista,elemento):
    '''
    Devuelve la cantidad de veces que aparece el elemento en la lista.
    '''
    n = 0
    for e in lista:
        if e == elemento:
            n += 1
    return n


def maximo(lista):
    '''
    Devuelve el máximo de una lista.
    '''
    m = -math.inf
    for e in lista:
        if e > m:
            m = e
    return m

def minimo(lista):
    '''
    Devuelve el minimo de una lista.
    '''
    m = math.inf
    for e in lista:
        if e < m:
            m = e
    return m
