'''Multiplicacion usando suma'''
def multiplicar(a,b):
    m = 0
    if a == 0 or b == 0:
        return 0
    else:
        for i in range(b):
            m += a
        return m

'''Creo lista con las multiplicaciones de a con numeros'''
def tabla(a,numeros):
    t = []
    for n in numeros:
        t.append(multiplicar(a,n))
    return t


numeros = list(range(10))

print(f'{0:>6d}{1:>3d}{2:>3d}{3:>3d}{4:>3d}{5:>3d}{6:>3d}{7:>3d}{8:>3d}{9:>3d}')
print('----------------------------------')

for n in numeros:
    idx = str(n) + ':'
    t = tabla(n,numeros)
    print(f'{idx}{t[0]:>4d}{t[1]:>3d}{t[2]:>3d}{t[3]:>3d}{t[4]:>3d}{t[5]:>3d}{t[6]:>3d}{t[7]:>3d}{t[8]:>3d}{t[9]:>3d}')
