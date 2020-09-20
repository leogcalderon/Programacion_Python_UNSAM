import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    '''
    Devuelve un array de un random walk de longitud: largo
    '''
    pasos=np.random.randint (-1,2,largo)
    return pasos.cumsum()


def plot_random_walks():
    ''''
    Simula 12 random walks, grafica los 12, luego grafica los que mas y menos se alejan.
    '''
    N = 100000
    random_walks = []

    plt.figure(figsize = (15,7))

    #Genera y grafica 12 random walks en el primer subplot
    f = plt.subplot(2, 1, 1)
    for i in range(12):
        random_walks.append(randomwalk(N))
        plt.plot(random_walks[i])
        plt.title('12 caminatas al azar')

    plt.xticks([])
    #Recupero los limites del primer subplot
    #asi los uso en los siguientes dos subplots
    ymin, ymax = f.get_ylim()

    #Busco los RW que mas y menos se alejan
    dic = {i:np.sum(abs(rw)) for i,rw in enumerate(random_walks)}
    menos_se_aleja = min(dic, key = dic.get)
    mas_se_aleja = max(dic, key = dic.get)

    #Plot del que menos se aleja
    plt.subplot(2, 2, 3)
    plt.plot(random_walks[menos_se_aleja])
    plt.ylim([ymin, ymax ])
    plt.xticks([])
    plt.title('Caminata que menos se aleja')

    #Plot del que mas se aleja
    plt.subplot(2, 2, 4)
    plt.plot(random_walks[mas_se_aleja])
    plt.ylim([ymin, ymax ])
    plt.xticks([])
    plt.title('Caminata que mas se aleja')

    plt.show()

if __name__ == '__main__':
    plot_random_walks()
