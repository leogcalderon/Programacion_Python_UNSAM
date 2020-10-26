import timeit as tt
import random
import matplotlib.pyplot as plt

def burbujeo(a):

    lista = a.copy()
    n = len(a)
    comparaciones = 0

    while n:
        for i in range(0, n - 1):
            if lista[i] < lista[i + 1]:
                continue
            else:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        n -= 1

    return lista

def mergesort(lista):

    if len(lista) > 1:
        medio = len(lista) // 2
        izq = mergesort(lista[:medio])
        der = mergesort(lista[medio:])

        return merge(izq, der)

    else:
        return lista

def merge(lista1, lista2):

    i, j = 0, 0
    resultado = []

    while (i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

def insercion(a):

    lista = a.copy()
    n = len(lista)

    for i in range(1, n):
        j = i
        while lista[j] < lista[j - 1] and j > 0:
            lista[j], lista[j - 1] = lista[j - 1], lista[j]
            j -= 1

    return lista


def seleccion(a):

    lista = a.copy()
    n = len(lista)
    ordenada = []

    while lista:
        menor = float('inf')
        for i in range(len(lista)):
            if lista[i] < menor:
                menor = lista[i]
        ordenada.append(menor)
        lista.remove(menor)

    return ordenada

def generar_lista(N):
    return [int(random.random()*1000) for _ in range(N)]


def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    """
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge = []

    global lista

    for lista in listas:

        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('seleccion(lista.copy())', number = num, globals = globals())
        tiempo_insercion = tt.timeit('insercion(lista.copy())', number = num, globals = globals())
        tiempo_burbujeo = tt.timeit('burbujeo(lista.copy())', number = num, globals = globals())
        tiempo_merge = tt.timeit('mergesort(lista.copy())', number = num, globals = globals())

        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_merge.append(tiempo_merge)

    return tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_merge

if __name__ == '__main__':

    listas = []

    for N in range(1, 256):
        listas.append(generar_lista(N))

    tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_merge = experimento_timeit_seleccion(listas, 10)

    plt.figure(figsize = (15,15))
    plt.plot(tiempos_seleccion, label = 'Seleccion')
    plt.plot(tiempos_burbujeo, label = 'Burbujeo')
    plt.plot(tiempos_insercion, label = 'Insercion')
    plt.plot(tiempos_merge, label = 'Merge')
    plt.xlabel('Longitud de lista')
    plt.ylabel('Tiempo')
    plt.legend()
    plt.show()
