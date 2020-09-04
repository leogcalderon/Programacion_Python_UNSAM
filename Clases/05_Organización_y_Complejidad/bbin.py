def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq | der | medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    maximo = lista[der]
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>4d} |{medio:4d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if pos == -1 and x > maximo:   # si no encontro y es mas grande que el maximo
        pos = medio + 1

    elif pos == -1 and x < maximo: # si no encontro y esta entre medio del min y max valor
        pos = medio

    return pos

def insertar(lista, x, verbose = True):

    if verbose:
        print(f'[DEBUG] izq | der | medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    maximo = lista[der]

    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>4d} |{medio:4d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if pos == -1 and x > maximo:   # si no encontro y es mas grande que el maximo
        pos = medio + 1
        lista.insert(pos, x) # agrega numero a la lista

    elif pos == -1 and x < maximo: # si no encontro y esta entre medio del min y max valor
        pos = medio
        lista.insert(pos, x) # agrega numero a la lista

    return pos, lista
