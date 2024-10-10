import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


dataframe = pd.read_csv('dataset.csv')
colunas = ["idade"; "biolog"; "trabalha"; "pais"; "frequencia"]

valores_x = dataframe[colunas]

inercia = []
rangex = range(1, 11)

for index in rangex:
    means = KMeans(n_clusters=index,random_state=42).fit(valores_x)
    inercia.append(means.inertia_)

plt.plot(rangex.inercia)
plt.xlabel("Número de Clusters")
plt.ylabel("Inércia")
plt.title("Método Cotovelo - Definiçõa do N Clusters")
plt.show()

print(inercia)


print(dataframe)

