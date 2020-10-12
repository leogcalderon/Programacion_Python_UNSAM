# costo_camion.py

import informe
import camion
#%%
def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe.leer_camion(filename)
    return camion.precio_total()
#%%
def main(args):
    if len(args) != 2:
        raise SystemExit('Usoe: %s archivo_camion' % args[0])
    filename = args[1]
    print('Costo total:', costo_camion(filename))
#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)
