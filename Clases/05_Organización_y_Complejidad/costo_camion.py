from tabla_informe import leer_camion

def costo_camion(nombre_archivo):
    '''Lectura de archivo'''
    camion = leer_camion(nombre_archivo)
    
    suma = 0
    '''Convertir a float y calcular total por fila'''
    for line in camion:
        try:
            suma += line['cajones']*line['precio']
        except ValueError:
                print('Missing value encontrado')

    return suma

'''Imprimimos resultado'''
cost = costo_camion('Data/camion.csv')
print('Total cost:', cost)