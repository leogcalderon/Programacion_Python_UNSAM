def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if e >= lista[medio]:
            res = bbinaria_rec(lista[medio:], e)
        else:
            res = bbinaria_rec(lista[:medio], e)
    return res
