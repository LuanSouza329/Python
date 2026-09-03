import pandas as pd
import os

produtos:list = ['Notebook', 'Mouse', 'Monitor', 'Teclado']
precos:list = [3500, 80, 1200, 250]


dados = {
    "produtos": produtos,
    "precos": precos
}

df = pd.DataFrame(dados)

indice_menor = df["precos"].idxmin()
indice_maior = df["precos"].idxmax()



print(df, "\n")
print(df['produtos'], "\n")
print("A maior preço é\n",  " ", df.loc[indice_maior])
print("A menor preço é\n",  " ", df.loc[indice_menor])
print(f"A média dos preços é {df['precos'].mean():.2f}")
print(f"A soma dos preços é {df['precos'].sum():.2f}")
print(df.loc[0, 'precos'])
print(df.loc[0])