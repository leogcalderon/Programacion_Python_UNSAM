import random
from burbujeo import burbujeo
from seleccion_insercion import seleccion, insercion
import matplotlib.pyplot as plt
from mergesort import sort_comparaciones

def generar_lista(N):
    return [int(random.random()*1000) for _ in range(N)]

if __name__ == '__main__':

    N = 256

    comparaciones_seleccion = []
    comparaciones_burbujeo = []
    comparaciones_insercion = []
    comparaciones_merge = []

    for i in range(1,N):

        lista = generar_lista(i)

        _, c_seleccion = seleccion(lista)
        _, c_burbujeo = burbujeo(lista)
        _, c_insercion = insercion(lista)
        _, c_merge = sort_comparaciones(lista)

        comparaciones_seleccion.append(c_seleccion)
        comparaciones_burbujeo.append(c_burbujeo)
        comparaciones_insercion.append(c_insercion)
        comparaciones_merge.append(c_merge)

    plt.figure(figsize = (15,5))
    plt.title('Comparaciones para lista de 256 de longitud')
    plt.plot(comparaciones_burbujeo, label = f'Burbujeo - {comparaciones_burbujeo[-1]} comparaciones')
    plt.plot(comparaciones_insercion, label = f'Insercion - {comparaciones_insercion[-1]} comparaciones')
    plt.plot(comparaciones_seleccion, label = f'Seleccion - {comparaciones_seleccion[-1]} comparaciones')
    plt.plot(comparaciones_merge, label = f'Merge - {comparaciones_merge[-1]} comparaciones')
    plt.legend()
    plt.show()
