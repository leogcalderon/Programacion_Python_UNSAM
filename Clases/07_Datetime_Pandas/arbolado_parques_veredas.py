import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Lectura de csv
df_veredas = pd.read_csv('Data/arbolado-publico-lineal-2017-2018.csv',
                         usecols = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol'])

df_parques = pd.read_csv('Data/arbolado-en-espacios-verdes.csv',
                         usecols = ['diametro','altura_tot','nombre_com'])

#Seleccionar Tipas
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'].copy()
df_tipas_parques = df_parques[df_parques['nombre_com'] == 'Tipa blanca'].copy()

#Renombrar columnas
df_tipas_veredas.rename(columns = {'nombre_cientifico':'nombre','altura_arbol':'altura','diametro_altura_pecho':'diametro'}, inplace = True)
df_tipas_parques.rename(columns = {'nombre_com':'nombre','altura_tot':'altura'}, inplace = True)

#Agregar ambiente a cada df
df_tipas_veredas['ambiente'] = 'vereda'
df_tipas_parques['ambiente'] = 'parque'

#Concatenar dos dataframe
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques], sort = False)

#Plotear
f, ax = plt.subplots(ncols = 2, figsize = (15,5))
df_tipas.boxplot('diametro',by = 'ambiente', ax = ax[0])
df_tipas.boxplot('altura',by = 'ambiente', ax = ax[1])
plt.show()
