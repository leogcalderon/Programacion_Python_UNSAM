'''Una pelota de goma es arrojada desde una altura de 100 metros
y cada vez que toca el piso salta 3/5 de la altura desde la que cayó.
Escribí un programa rebotes.py que imprima una tabla mostrando las alturas
que alcanza en cada uno de sus primeros diez rebotes.'''

altura = 100
reduccion = 3/5
rebote = 1

while rebote <= 10:
    altura *= reduccion
    print((rebote),round(altura,4))
    rebote += 1
