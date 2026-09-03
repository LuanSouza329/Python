import pandas as pd

dados = {
    "vendedor": [
        "Ana",
        "Carlos",
        "Ana",
        "Maria",
        "Carlos"
    ],
    "vendas": [
        100,
        200,
        150,
        300,
        250
    ]
}

df = pd.DataFrame(dados)

print(df.sort_values("vendas")) # Ordena o Dataframe pela coluna de vendas em ordem crescente


print(df.sort_values( # Ordena o Dataframe pela coluna de vendas em ordem decrescente
    "vendas",
    ascending=False
))

print(
    df.groupby("vendedor")["vendas"].sum() # Agrupa o Dataframe pelo vendedor e soma as vendas de cada um
)

print(
    df.groupby("vendedor")["vendas"].mean() # Agrupa o Dataframe pelo vendedor e calcula a média das vendas de cada um
)

print(
    df.groupby("vendedor")["vendas"].sum() > 300
)

vendas_por_vendedor = df.groupby("vendedor")["vendas"].sum()

print(vendas_por_vendedor.idxmax())

vendas_por_vendedor = (
    df.groupby("vendedor")["vendas"].sum()
)

print(
    vendas_por_vendedor[
        vendas_por_vendedor > 300
    ]
)