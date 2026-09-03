import pandas as pd

dados = {
    "produto": ["Notebook", "Mouse", "Monitor", "Teclado"],
    "preco": [3500, None, 1200, None]
}

df = pd.DataFrame(dados)

nulos = df.isna().sum()
media_preco = df[df['preco'].notna()]['preco'].mean()

df['preco'] = df['preco'].fillna(media_preco)


print(f"Número de valores ausentes por coluna:\n{nulos} \n")
print(f"A média de preços existentes: \n {media_preco}")
print(df["preco"])