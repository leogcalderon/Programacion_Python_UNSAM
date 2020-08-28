import csv

def leer_arboles(nombre_archivo):

    arboleda = []

    file = open(nombre_archivo,'rt')
    rows = csv.reader(file)
    headers = next(rows)
    types = [float,float,
             int,int,int,int,int,
             str,str,str,str,str,str,str,str,
             float,float]

    for row in rows:
        dic = {header : func(val) for header,func,val in zip(headers,types,row)}
        arboleda.append(dic)

    return arboleda

def medidas_de_especies(especies,arboleda):

    medidas = {}

    for e in especies:
        H = [(float(arbol['altura_tot']) , float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == e]
        medidas[e] = H

    return medidas

arboleda = leer_arboles('Data/arbolado-en-espacios-verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas  = medidas_de_especies(especies,arboleda)

for e in especies:
    print(e)
    print('Cantidad de registros:',len(medidas[e]),'\n')
