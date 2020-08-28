import numpy as np
import matplotlib.pyplot as plt

lecturas = np.load('Data/Temperaturas.npy')

plt.figure(figsize=(7,7))
plt.hist(lecturas, bins=99)
plt.show()
