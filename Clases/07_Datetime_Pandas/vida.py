import datetime
import sys

def segundos_vividos(fecha):
    '''
    Devuelve los segundos transcurridos desde fecha hasta hoy
    fecha = dd/mm/yyyy
    '''
    fecha = [int(x) for x in fecha.split('/')]
    fecha = datetime.datetime(fecha[2],fecha[1],fecha[0])
    hoy = datetime.datetime.now()

    return int((hoy - fecha).total_seconds())

if __name__ == '__main__':
    segundos = segundos_vividos(sys.argv[1])
    print('Segundos vividos:',segundos)
