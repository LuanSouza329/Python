import pandas as pd

vendas_janeiro = pd.DataFrame({
    "id": [1, 2, 3],
    "produto": ["Notebook", "Mouse", "Monitor"],
    "valor": [3500, 80, 1200]
})

vendas_fevereiro = pd.DataFrame({
    "id": [4, 5, 6],
    "produto": ["Teclado", "Notebook", "Mouse"],
    "valor": [250, 4000, 100]
})

vendas_marco = pd.DataFrame({
    "id": [7, 8],
    "produto": ["Monitor", "Notebook"],
    "valor": [1500, 4200],
    "cidade": ["SP", "RJ"]
})


df = pd.concat(
    [vendas_janeiro, vendas_fevereiro, vendas_marco],
    ignore_index= True,
)



print(df.head(), '\n\n')
print(df.shape, '\n\n')
print(df.info(), '\n\n')
print(df.isnull().sum(), '\n\n')
print(df['produto'].value_counts(), '\n\n')
print(df["produto"].value_counts(normalize=True))
