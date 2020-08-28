import random
import numpy as np

temperatura_real = 37.5
lecturas = []
for _ in range(999):
    error = random.normalvariate(0,0.2)
    lecturas.append(temperatura_real + error)

max_t = np.max(lecturas)
min_t = np.min(lecturas)
avg = sum(lecturas)/len(lecturas)
median = sorted(lecturas)[int(len(lecturas)/2)]

array = np.array(lecturas)
np.save('Data/Temperaturas.npy',array)

print('Max =',max_t,'\nMin =',min_t,'\nPromedio =',avg,'\nMediana =',median)
