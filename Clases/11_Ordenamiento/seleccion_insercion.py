def insercion(a):

    lista = a.copy()
    n = len(lista)
    comparaciones = 0

    for i in range(1, n):
        j = i
        while lista[j] < lista[j - 1] and j > 0:
            lista[j], lista[j - 1] = lista[j - 1], lista[j]
            j -= 1
            comparaciones += 1

    return lista, comparaciones


def seleccion(a):

    lista = a.copy()
    n = len(lista)
    ordenada = []
    comparaciones = 0

    while lista:
        menor = float('inf')
        for i in range(len(lista)):
            if lista[i] < menor:
                menor = lista[i]
            comparaciones += 1
        ordenada.append(menor)
        lista.remove(menor)

    return ordenada, comparaciones
