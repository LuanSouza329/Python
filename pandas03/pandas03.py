import pandas as pd

produtos = {
    "produto": ["Notebook", "Mouse", "Monitor", "Teclado"],
    "preco": [3500, 80, 1200, 250]
}

df = pd.DataFrame(produtos)


print(df.loc[1]) #seleciona a linha 1

print(df.iloc[1]) #seleciona a linha 1 usando o indice inteiro

print(df.loc[2, 'preco'])

print(df.loc[[0,2], ['produto', 'preco']]) #Seleciona as linhas 0 e 2 e as colunas produto e preço

print(df.loc[
    [0, 2], ['produto']
])