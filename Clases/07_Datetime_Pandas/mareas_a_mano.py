import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Leer dataset
df = pd.read_csv('https://raw.githubusercontent.com/python-unsam/UNSAM_2020c2_Python/master/Notas/07_Fechas_Carpetas_y_Pandas/OBS_SHN_SF-BA.csv',
                 index_col = ['Time'], parse_dates=True)

dh = df['12-25-2014':].copy()

errors = {}

#Itero para un rango de dt y dh, calculo el error y lo agrego a un diccionario
for d_t in np.arange(-5,5,1):
    for d_h in np.arange(0,30,0.1):
        temp_df = pd.DataFrame([dh['H_SF'].shift(d_t) - d_h, dh['H_BA']]).T.dropna()
        temp_df['diff'] = temp_df['H_SF'] - temp_df['H_BA']
        errors[(d_t, d_h)] = np.sum(abs(temp_df['diff']))

#Busco el error minimo y los parametros
min_error = errors[sorted(errors, key = errors.get)[0]]
min_params = sorted(errors, key = errors.get)[0]

#Grafico y devuelvo error - parametros
print('Min error:',min_error)
print('Parameters:\n- dt:',min_params[0],'\n- dh:',min_params[1])
pd.DataFrame([dh['H_SF'].shift(min_params[0]) - min_params[1], dh['H_BA']]).T.plot()
plt.show()
