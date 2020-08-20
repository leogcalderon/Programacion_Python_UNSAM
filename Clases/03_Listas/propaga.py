def buscar_elemento(lista,elemento):
    '''
    Busca posiciones del elemento en lista
    '''
    idx = []
    for i, e in enumerate(lista):
        if lista[i] == elemento:
            idx.append(i)
    return idx


def propagar_adyacentes(lista):
    '''
    Creo copia de la lista para ir modificandola
    '''
    propagado = lista.copy()

    '''
    Busco indices de los que estan prendidos
    '''
    idx_prendidos = buscar_elemento(lista,1)

    '''
    Modifico los fosforos adyacentes
    '''
    for idx in idx_prendidos:
        if idx != 0:
            if lista[idx-1] == 0:
                propagado[idx-1] = 1
        if idx != (len(lista) - 1):
            if lista[idx+1] == 0:
                propagado[idx+1] = 1

    return propagado


def buscar_no_encendidos(lista):
    '''
    Devuelve True si hay fosforos 0 al lado de fosforos 1.
    '''
    faltan = False

    for i,e in enumerate(lista):
        '''Primer fosforo'''
        if i == 0:
            if e == 0 and lista[i+1] == 1:
                faltan = True

        '''Ultimo fosforo'''
        if i == (len(lista) - 1):
            if e == 0 and lista[i-1] == 1:
                faltan = True

        '''Fosforos intermedios'''
        if i != 0 and i != (len(lista) - 1):
            if (e == 0 and lista[i-1] == 1) or (e == 0 and lista[i+1] == 1):
                faltan = True

    return faltan


def propagar(lista):
    '''
    Mientras falten potenciales fosforos (0 al lado de 1)
    sigo propagando.
    '''
    faltan = True

    while faltan:
        lista = propagar_adyacentes(lista)
        faltan = buscar_no_encendidos(lista)

    return lista
