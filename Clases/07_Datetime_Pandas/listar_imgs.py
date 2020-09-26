import os
import sys
import pprint

def listar_imagenes(dir):
    '''
    Devuelve una lista de los archivos .png que se
    encuentren en los subdirectorios del directorio dado
    '''

    subdirectorios = os.listdir(dir) #Lista todos los subdirectorio del dir
    imagenes = []

    for subdir in subdirectorios:
        #Si el path es un directorio
        if os.path.isdir(os.path.join(dir,subdir)):
            #Lista archivos del subdirectorio
            archivos_subdirectorio = os.listdir(os.path.join(dir,subdir))
            for archivo in archivos_subdirectorio:
                #Si el archivo es imagen, agrego a lista
                if archivo.endswith('.png'):
                    imagenes.append(archivo)

    pprint.pprint(imagenes)

if __name__ == '__main__':
    listar_imagenes(sys.argv[1])
