
altura = 100
reduccion = 3/5
rebote = 1

while rebote <= 10:
    altura *= reduccion
    print((rebote),round(altura,4))
    rebote += 1

'''
OUTPUTS:
1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
'''
