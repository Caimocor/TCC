import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import ones,vstack
from numpy.linalg import lstsq

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

print(x_inicial)
print(y_inicial)
print(x_final)
print(y_final)


X = np.append(x_inicial,x_final)
Y = np.append(y_inicial,y_final)

#plot os pontos
plt.scatter(X, Y,s=1)




plt.show()




