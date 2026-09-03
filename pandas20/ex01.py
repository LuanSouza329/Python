import pandas as pd

df = pd.DataFrame({
    "produto": [
        "Notebook",
        "Mouse",
        "Notebook",
        "Monitor",
        "Mouse",
        "Notebook",
        "Teclado"
    ],
    "cidade": [
        "SP",
        "RJ",
        "SP",
        "BH",
        "RJ",
        "SP",
        "BH"
    ],
    "vendedor": [
        "Ana",
        "Carlos",
        "Ana",
        "Maria",
        "Carlos",
        "Ana",
        "Maria"
    ]
})

#Análise exploratória dos dados
print(df.head())
print(df.shape, '\n\n')
print(df.info(), '\n\n')
print(df.isna().sum(),'\n\n')

#Análise das colunas
print(df['produto'].unique(), '\n\n')
print(df['produto'].nunique(), '\n\n')
print(df['produto'].value_counts(), '\n\n')
print(df['cidade']
      .value_counts(normalize=True)
      .mul(100)
      .round(2)
    )
