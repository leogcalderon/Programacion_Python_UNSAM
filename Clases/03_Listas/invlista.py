def invertir_lista(lista):
    '''
    Dada una lista devuelve otra que tiene
    los mismos elementos pero en el orden inverso.
    '''
    invertida = []
    for i,e in enumerate(lista):
        invertida.append(lista[len(lista) - 1 - i])
    return invertida
