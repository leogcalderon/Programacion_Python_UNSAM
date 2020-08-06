saldo = 500000
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0
'''
Variables para pago extra por meses
'''
pago_extra = 1000
meses = 0
'''
Variables para pago extra durante cuatro años
'''
pago_extra_mes_comienzo = 60
pago_extra_mes_fin = pago_extra_mes_comienzo + 12*4

while saldo > 0:

    if meses >= pago_extra_mes_comienzo and meses < pago_extra_mes_fin:
        '''Mes con pago extra'''
        if saldo < (pago_mensual + pago_extra):
            '''Pago final'''
            total_pagado += saldo
            saldo = 0
        else:
            '''Pago normal'''
            saldo = saldo*(1 + tasa/12) - pago_mensual - pago_extra
            total_pagado = total_pagado + pago_mensual + pago_extra

    else:
        '''Mes sin pago extra'''
        if saldo < (pago_mensual):
            '''Pago final'''
            total_pagado += saldo
            saldo = 0
        else:
            '''Pago normal'''
            saldo = saldo*(1 + tasa/12) - pago_mensual
            total_pagado = total_pagado + pago_mensual

    meses += 1

    '''Creación de tabla'''
    print(meses,round(total_pagado,2), round(saldo,2))

print('Total pagado:',round(total_pagado,2))
print('Meses:',meses)

'''
OUTPUTS:
1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
...
308 874705.88 3478.83
309 877389.99 809.21
310 878199.2 0
Total pagado: 878199.2
Meses: 310
'''
