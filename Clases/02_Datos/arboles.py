import csv
from collections import Counter

def leer_parque(nombre_archivo,parque):
    '''Lectura de archivo'''
    lista = []
    file = open(nombre_archivo,'rt')
    rows = csv.reader(file)
    headers = next(rows)
    
    for row in rows:
        '''Si la fila pertenece al parque, adjunto fila'''
        if row[10].lower() == parque.lower():
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

def especies(lista_arboles):
    especies = set()
    for arbol in lista_arboles:
        especies.add(arbol['nombre_com'])
    return especies


def contar_ejemplares(lista_arboles):
    cuenta = Counter()
    for arbol in lista_arboles:
        cuenta[arbol['nombre_com']] += 1
    return cuenta

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'].lower() == especie.lower():
            alturas.append(arbol['altura_tot'])
    return alturas

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'].lower() == especie.lower():
            inclinaciones.append(arbol['inclinacio'])
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    esp = especies(lista_arboles)
    max_inclinacion = ['',0]
    for e in esp:
        i = max(obtener_inclinaciones(lista_arboles,e))
        if i > max_inclinacion[1]:
            max_inclinacion = [e,i]
    return max_inclinacion
    
def especie_promedio_mas_inclinada(lista_arboles):
    esp = especies(lista_arboles)
    promedios = ['',0]
    for e in esp:
        i = obtener_inclinaciones(lista_arboles,e)
        p = sum(i) / len(i)
        if p > promedios[1]:
            promedios = [e,p]
    return promedios
