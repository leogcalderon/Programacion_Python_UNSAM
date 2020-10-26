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
    comparaciones = 0

    while (i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        comparaciones += 1

    comparaciones_l.append(comparaciones)

    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado


def sort_comparaciones(lista):
    global comparaciones_l
    comparaciones_l = []
    sorted = mergesort(lista)
    return sorted, sum(comparaciones_l)
