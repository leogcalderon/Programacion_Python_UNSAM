from collections import Counter
import random

def naipe():
    '''Crea naipe'''
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    return naipes

def puntos(cartas):
    '''Puntos de una mano de truco'''
    puntos = 0

    '''Si tenemos dos o mas con la misma pinta'''
    if Counter([x[1] for x in cartas]).most_common()[0][1] >= 2:

        '''Selecciono la pinta repetida'''
        pinta_repetida = Counter([x[1] for x in cartas]).most_common()[0][0]
        puntos += 20

        if Counter([x[1] for x in cartas]).most_common()[0][1] == 2:
            '''Solo dos de la misma pinta'''
            for valor,palo in cartas:
                if palo == pinta_repetida:
                    if valor <= 7:
                        puntos += valor

        else:
            '''Tres de la misma  pinta'''
            '''Selecciono las cartas mas altas'''
            if all([x[0]>7 for x in cartas]):
                '''Si todas son negras devuelvo 20'''
                puntos += 20
            else:
                mayor_valor = sorted([x[0] for x in cartas if x[0] <= 7])[-2:]
                if len(mayor_valor) == 2:
                    '''Dos que no son negras'''
                    puntos += mayor_valor[0] + mayor_valor[1]
                else:
                    '''Una que no es negra'''
                    puntos += mayor_valor[0]
    else:
        '''Si no tenemos dos de la misma pinta'''
        if all([x[0]>7 for x in cartas]):
            '''Si todas son negras devuelvo 0'''
            return puntos

        else:
            '''Devuelvo la mas grande'''
            puntos = max([x[0] for x in cartas if x[0] <= 7])

    return puntos

def prob(X,n):
    '''Probabilidad de sacar X puntos'''
    cuenta = 0
    naipes = naipe()

    for _ in range(n):

        cartas = random.sample(naipes,k=3)
        p = puntos(cartas)

        if p == X:
            cuenta += 1

    prob = cuenta/n

    return prob


'''
OUTPUTS
prob(31,1000000) = 0.029353
prob(32,1000000) = 0.015
prob(33,1000000) = 0.015412
'''
