#esse codigo tem como objetivo implementar um grafo
#utilizando as coordenadas que estão marcadas no CSV
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from math import hypot
import networkx as nx
import plotly.plotly as py
import plotly.tools as tls

import matplotlib.pyplot as plt

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

X = np.append(x_inicial,x_final)
Y = np.append(y_inicial,y_final)

G=nx.Graph()
for i in range(0,len(X),2):

    G.add_edge((X[i],Y[i]),(X[i+1],Y[i+1]))

    
#armazena os componentes do grafo num vetor
graphs = list(nx.connected_components(G))


print('Nós',len(list(G.nodes)))
print('Arestas',len(list(G.edges)))
print('Grafo está conectado?',nx.is_connected(G))
print('Numero de componentes',nx.number_connected_components(G))


size_component = []
for g in graphs:
    size_component.append(len(g))

new_a = sorted(set(size_component), key=size_component.index)



#quantidade de elementos de cada elemento
qt_elements =[]
for a in new_a:
    qt_elements.append(size_component.count(a))
print(qt_elements)










