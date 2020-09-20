def valor_absoluto(n):
    '''
    Calcula valor absoluto de un numero
    Precondicion: n debe ser un numero (int/float)
    Poscondicion: devuelve el valor absoluto de n
    '''
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    '''
    Suma numeros pares
    Precondicion: l debe ser un iterable
    Poscondicion: devuelve la suma de los elementos pares en l (key en caso de ser diccionario)
    '''
    res = 0 #Invariante de ciclo
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''
    Multiplica dos numeros
    Precondicion: a puede ser (int/float), b debe ser (int)
    Poscondicion: devuelve la multiplicación de a con b
    '''
    res = 0 #invariante de ciclo
    nb = b #invariante de ciclo
    while nb != 0:
        res += a
        nb -= 1 #Si b = float, nunca alcanza el estado nb != 0
    return res

def collatz(n):
    '''
    Calcula pasos de la función de Collatz
    Precondicion: n debe ser un numero entero positivo
    Poscondicion: devuelve el numero de pasos realizados hasta llegar a n = 1
    '''
    res = 1 #Invariante de ciclo

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
