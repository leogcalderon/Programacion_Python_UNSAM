
import csv

def costo_camion(nombre_archivo):
    '''Lectura de archivo'''
    file = open(nombre_archivo,'rt')
    rows = csv.reader(file)
    headers = next(rows)
    suma = 0

    try:
        '''Convertir a float y calcular total por fila'''
        for line in rows:
            line[-1] = float(line[-1])
            line[-2] = float(line[-2])
            suma += line[-1]*line[-2]

    except ValueError:
        print('Missing values encontrados')

    file.close()

    return suma
