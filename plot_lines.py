import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from math import hypot

#le o dataframe considerando o separador como ;
df = pd.read_csv('dados/PR_antigo.csv',  sep=";")

#adiciona os valores das coordenadas x e y como um numpy array
x_inicial = np.array(df.loc[:,['COORD_X_INIC_PR']].values[:,0])
y_inicial = np.array(df.loc[:,['COORD_Y_INIC_PR']].values[:,0])
x_final = np.array(df.loc[:,['COORD_X_FIM_PR']].values[:,0])
y_final = np.array(df.loc[:,['COORD_Y_FIM_PR']].values[:,0])



#troca a virgula que separa as casas decimais para ponto
for i  in range(len(x_inicial)):
    x_inicial[i] = x_inicial[i].replace(',','.')
    y_inicial[i] = y_inicial[i].replace(',','.')
    x_final[i] = x_final[i].replace(',','.')
    y_final[i] = y_final[i].replace(',','.')
    
#converte os dados para float
x_inicial = np.asarray(list(map(float, x_inicial)))
y_inicial = np.asarray(list(map(float, y_inicial)))
x_final = np.asarray(list(map(float, x_final)))
y_final = np.asarray(list(map(float, y_final)))

x = np.append(x_inicial,x_final)
y = np.append(y_inicial,y_final)

it = np.nditer(x_inicial,flags=['f_index'])


for i in it:
    if it.index % 2000 == 0:
        print(it.index)
    plt.plot([x_inicial[it.index],x_final[it.index]], [y_inicial[it.index],y_final[it.index]], 'ro-')

plt.show()





