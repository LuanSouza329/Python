import pandas as pd

df = pd.DataFrame({
    "vendedor": [
        "Ana", "Carlos", "Ana", "Maria",
        "Carlos", "Ana", "Maria"
    ],
    "produto": [
        "Notebook", "Mouse", "Notebook", "Monitor",
        "Mouse", "Teclado", "Monitor"
    ],
    "cidade": [
        "SP", "RJ", "SP", "BH",
        "RJ", "SP", "BH"
    ]
})

print(df['cidade'].nunique(), '\n\n') #Quantos unicos
print(df['cidade'].unique(), '\n\n') #Quais unicos
print(df['cidade'].value_counts(), '\n\n')
print(df["cidade"].value_counts(normalize=True), '\n\n')

print((
    df["cidade"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
))

print(df.head(), '\n\n')
print(df.shape, '\n\n')
print(df.info(), '\n\n')
print(df.isnull().sum(), '\n\n')
print(df.isna().sum(), '\n\n')
