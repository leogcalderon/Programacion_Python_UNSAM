import random
from collections import Counter

def tirar(N):
    '''Tira N dados'''
    numeros = [random.randint(1,6) for _ in range(N)]
    return numeros

def es_generala(tirada):
    '''Devuelve true si los N dados son iguales'''
    return all([x == tirada[0] for x in tirada])

def generala():
    '''Tira 5 dados, se queda con los que son iguales y tira dados 2 rondas mas.'''
    dados = tirar(5)
    tirada = es_generala(dados)
    turnos = 1

    while not tirada and turnos < 3:
        numero, cantidad = Counter(dados).most_common()[0]
        me_quedo = [numero]*cantidad
        dados_a_tirar = 5 - len(me_quedo)
        dados = tirar(dados_a_tirar) + me_quedo
        tirada = es_generala(dados)
        turnos += 1

    return tirada

def probabilidad_generala(n):
    '''Probabilidad de ganar en tres tiradas'''
    gano = 0

    for _ in range(n):
        if generala():
            gano += 1
            
    prob = gano/n

    return prob
