frase = str(input('Ingrese frase:'))
nueva_frase = ''
palabras = frase.split()

for palabra in palabras:
    nueva_palabra = ''

    if len(palabra) > 1:
        if palabra[-1] == 'o':
            '''Si la palabra finaliza en o'''
            nueva_palabra = palabra[:-1] + 'e'

        elif palabra[-2] == 'o':
            '''Si la penultima palabra termina en o'''
            nueva_palabra = palabra[:-2] + 'e' + palabra[-1]

        else:
            '''No corresponde un cambio de letra'''
            nueva_palabra = palabra
    else:
        nueva_palabra = palabra

    nueva_frase += nueva_palabra + ' '

print(nueva_frase)

'''
OUTPUTS:
- Los hermanos sean unidos porque ésa es la ley primera
- Les hermanes sean unides porque ésa es la ley primera

- ¿cómo transmitir a los otros el infinito Aleph?
- ¿cóme transmitir a les otres el infinite Aleph?

- Todos, tu también
- Todos, tu también
'''
