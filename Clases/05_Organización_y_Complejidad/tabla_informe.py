from fileparse import parse_csv

def leer_camion(nombre_archivo):
    '''Lectura de archivo'''
    camion = parse_csv(nombre_archivo, select=['nombre','cajones','precio'], types=[str,int,float])
    return camion

def leer_precios(nombre_archivo):
    '''Lectura de archivo'''
    precios = parse_csv('Data/precios.csv', types=[str,float], has_headers=False)
    precios = {p[0]:p[1] for p in precios}
    return precios

def hacer_informe(archivo_camion,archivo_precios):
    
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    
    productos = []
    headers = ['Nombre','Cajones','Precio','Cambio']
    
    for i in camion:
        cambio = precios[i['nombre']] - i['precio'] 
        tupla = (i['nombre'],i['cajones'],i['precio'],cambio)
        productos.append(tupla)

    print(f'{headers[0]:>12s}{headers[1]:>10s}{headers[2]:>10s}{headers[3]:>10s}')
    print('  ---------- ---------- ---------- ----------')
    for nombre,cajones,precio,cambio in productos:
        precio = '$' + str(round(precio,2))
        print(f'{nombre:>12s}{cajones:>10d}{precio:>10s}{cambio:>10.2f}')


'''
OUTPUT:
    
          Nombre   Cajones    Precio    Cambio
  ---------- ---------- ---------- ----------
        Lima       100     $32.2      8.02
     Naranja        50     $91.1     15.18
       Caqui       150   $103.44      2.02
   Mandarina       200    $51.23     29.66
     Durazno        95    $40.37     33.11
   Mandarina        50     $65.1     15.79
     Naranja       100    $70.44     35.84

'''