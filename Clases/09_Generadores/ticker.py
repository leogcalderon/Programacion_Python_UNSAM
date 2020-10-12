from vigilante import vigilar
import csv
import informe
import formato_tabla

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def ticker(path_camion, path_mercado, formato):
    camion = informe.leer_camion(path_camion)
    filas = parsear_datos(vigilar(path_mercado))
    filas = filtrar_datos(filas, camion)
    formateador = formato_tabla.crear_formateador(formato)
    formateador.encabezado(['nombre', 'precio', 'volumen'])
    for fila in filas:
        fila = [str(x) for x in fila.values()]
        formateador.fila(fila)
