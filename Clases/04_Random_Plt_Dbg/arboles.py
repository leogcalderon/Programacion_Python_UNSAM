import csv
from collections import Counter
import os
import matplotlib.pyplot as plt

path = os.path.join('Data', 'arbolado-en-espacios-verdes.csv')

def leer_arboles(nombre_archivo,especie):
    '''Lectura de archivo'''
    lista = []
    file = open(nombre_archivo,'rt')
    rows = csv.reader(file)
    headers = next(rows)

    for row in rows:
        '''Si la fila pertenece al parque, adjunto fila'''
        if row[7].lower() == especie.lower():
            arbol = {}
            '''Verifico type'''
            for columna, nombre in zip(row,headers):
                if nombre in ['long','lat','coord_x','coord_y']:
                    arbol[nombre] = float(columna)
                elif nombre in ['id_arbol','altura_tot','diametro','inclinacio','id_especie']:
                    arbol[nombre] = int(columna)
                else:
                    arbol[nombre] = columna
            lista.append(arbol)
    return lista

arboleda = leer_arboles(path,'Jacarandá')
altos = [x['altura_tot'] for x in arboleda]
diametros = [x['diametro'] for x in arboleda]

f, ax = plt.subplots(ncols = 2, figsize=(15,15))
ax[0].hist(altos, bins = 'auto')
ax[0].set_title('Histograma de altura - Jacarandá')
ax[0].set_xlabel('Altura (m)')
ax[0].set_ylabel('Frecuencia')

ax[1].scatter(diametros,altos)
ax[1].set_title('Relacion diametro altura - Jacarandá')
ax[1].set_xlabel('Diametro (cm)')
ax[1].set_ylabel('Altura (m)')
plt.show()
