import random
import numpy as np

################################################################################
###############################   FIGURITAS ####################################
################################################################################

def crear_album(figus_total):
    '''Crea album'''
    return np.zeros((figus_total))

def album_incompleto(album):
    '''Verifica si nos falta alguna figurita'''
    return any([x==0 for x in album])

def comprar_figu(figus_total):
    '''Devuelve una figurita'''
    return random.randint(0,figus_total-1)

def cuantas_figus(figus_total):
    '''Cuantas figuritas comprar para llenar el album'''
    album = crear_album(figus_total)
    compras = 0

    while album_incompleto(album):
        album[comprar_figu(figus_total)] = 1.
        compras += 1

    return compras

#Ejercicio 4.19
compras_6 = np.mean([cuantas_figus(6) for _ in range(1000)]) #Output: 14.76

#Ejercicio 4.20
compras_670 = np.mean([cuantas_figus(670) for _ in range(100)])  #Output 4809.83

################################################################################
###############################   PAQUETES #####################################
################################################################################

def comprar_paquete(figus_total, figus_paquete):
    '''Devuelve paquete'''
    return [random.randint(0,figus_total-1) for _ in range(figus_paquete)]

def cuantos_paquetes(figus_total, figus_paquete):
    '''Cuenta de cuantos paquetes para llenar album'''
    album = crear_album(figus_total)
    compras = 0

    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for fig in paquete:
            album[fig] = 1
        compras += 1

    return compras

# Ejercicio 4.24
compras_paquetes = np.mean([cuantos_paquetes(670,5) for _ in range(1000)]) #Output 960.37
