import pandas as pd

df = pd.read_csv("alunos.csv")

print(df) #Imprime o DataFrame inteiro
print('A maior idade é: ' + str(max(df['idade']))) #imprime a maior idade
print(df.shape) #Imprime a quantidade de Linhas e Colunas do Dataframe
print(df.columns) #Imprimeo nome das colunas do Dataframe
print(df.dtypes) #Imprime o tipo de cada coluna do Dataframe
print(df.info()) #Imprime um resumo do DataFrame, incluindo o número de entradas, colunas, tipos de dados e uso de memória

print(df[['nome', 'idade']]) #Imprime apenas as colunas selecionadas do Dataframe
print(df['idade'].mean()) #Imprime a média da coluna idade do Dataframe
print(df['idade'].min())
print(df['idade'].max())
print(df['idade'].sum())

print(df['idade'].sum() / df['idade'].count())