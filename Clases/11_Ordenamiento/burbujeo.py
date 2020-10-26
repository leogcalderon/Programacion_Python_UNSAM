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
            comparaciones += 1
        n -= 1

    return lista, comparaciones

'''
(n-1) comparaciones en el primer paso, (n-2) en el segundo ...
Numero total de comparaciones = (n-1) + (n-2) + ... + 3 + 2 + 1 = n(n-1)/2 = O(n^2)
'''
