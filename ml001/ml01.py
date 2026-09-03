import pandas as pd

#Framework de aprendizado de máquina
from sklearn import cluster
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#Carregando os dados do arquivo CSV
df = pd.read_csv('dados_clientes.csv')

# Exemplo para 2 casas decimais. Análise exploratório dos dados
print(df[['idade', 'renda_anual', 'pontuacao_gastos']].describe().round(2))

padronizador = StandardScaler()

dados_padronizados = padronizador.fit_transform(df[['idade', 'renda_anual', 'pontuacao_gastos']])

print('\n', dados_padronizados)

k = 3

kmeans = KMeans(n_clusters = k)

kmeans.fit(dados_padronizados)

df['cluster'] = kmeans.labels_

print('\n', df.head(10))

df.to_csv('dados_clientes.csv', index=False)