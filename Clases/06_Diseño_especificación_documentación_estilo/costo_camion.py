import csv
import sys

def costo_camion(nombre_archivo):
    '''Lectura de archivo'''
    file = open(nombre_archivo,'rt')
    rows = csv.reader(file)
    headers = next(rows)
    suma = 0


    '''Convertir a float y calcular total por fila'''
    for line in rows:
        try:
            line[-1] = float(line[-1])
            line[-2] = float(line[-2])
            suma += line[-1]*line[-2]
        except ValueError:
                print('Missing value encontrado')

    file.close()

    return suma

def main(nombre_archivo):
    cost = costo_camion(nombre_archivo)
    print('Total cost:', cost)

if __name__ == '__main__':
    main(sys.argv[1])
