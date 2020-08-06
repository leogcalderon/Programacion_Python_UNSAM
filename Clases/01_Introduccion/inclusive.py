frase = str(input('Ingrese frase:'))
nueva_frase = ''
palabras = frase.split()

for palabra in palabras:
    nueva_palabra = ''

    if palabra[-1] == 'o':
        '''Si la palabra finaliza en o'''
        nueva_palabra = palabra[:-1] + 'e'

    elif palabra[-2] == 'o':
        '''Si la penultima palabra termina en o'''
        nueva_palabra = palabra[:-2] + 'e' + palabra[-1]

    else:
        '''No corresponde un cambio de letra'''
        nueva_palabra = palabra

    nueva_frase += nueva_palabra + ' '

print(nueva_frase)
