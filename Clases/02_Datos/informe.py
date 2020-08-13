import csv

def leer_camion(nombre_archivo):
    '''Lectura de archivo'''
    file = open(nombre_archivo,'rt')
    rows = csv.reader(file)
    _ = next(rows)
    camion = []

    for row in rows:
        try:
            temp_dict = {}
            temp_dict['nombre'] = row[0]
            temp_dict['cajones'] = int(row[1])
            temp_dict['precio'] = float(row[2])
            camion.append(temp_dict)
        except:
            print('Missing value encontrado')

    file.close()

    return camion

def leer_precios(nombre_archivo):
    '''Lectura de archivo'''
    file = open(nombre_archivo,'rt')
    rows = csv.reader(file)
    precios = {}

    for row in rows:
        try:
            precios[row[0]] = float(row[1])
        except:
            pass

    return precios


def balance(data_camion,data_precios):
    '''Generamos los dos diccionarios'''
    camion = leer_camion(data_camion)
    precios = leer_precios(data_precios)

    '''Calculo del costo y ventas'''
    costo = 0
    venta = 0
    for c in camion:
        costo += c['cajones']*c['precio']
        venta += c['cajones']*precios[c['nombre']]

    diferencia = round(venta - costo,2)
    
    if diferencia > 0:
        print('Ganancia')
    else:
        print('Pérdida')

    print('Costo: $',costo,'\nVenta: $',venta,'\nDiferencia: $',diferencia)
