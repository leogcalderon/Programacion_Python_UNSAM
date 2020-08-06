palabra = str(input('Ingrese palabra:'))
vocales = ['a','e','i','o','u']
nueva_palabra = ''

for letra in palabra:
    if letra in vocales:
        '''Si la letra es vocal, agrega p + letra'''
        nueva_palabra += letra + 'p' + letra
    else:
        '''Si no es vocal, agrega la letra'''
        nueva_palabra += letra

print(nueva_palabra)
