import pandas as pd

df = pd.read_csv('dados.csv')

df['faturamento'] = (
    df['preco_unitario'] *
    df['quantidade']
)

print(df.head(), '\n\n\n')

df["total_cliente"] = (
    df.groupby("cliente")["faturamento"]
      .transform("sum")
)

df['percentual_cliente'] = (
    (df['faturamento'] / df['total_cliente'])
    * 100
).round(2)

df["media_categoria"] = (
    df.groupby("categoria")["faturamento"]
      .transform("mean")
      .round(2)
)

df['desvio_da_media'] = (
    df['faturamento'] - df['media_categoria']
)

df["media_vendedor"] = (
    df.groupby("vendedor")["faturamento"]
      .transform("mean")
      .round(2)
)
    
df["acima_media"] = (
    df["faturamento"] > df["media_vendedor"]
).map({
    True: "Sim",
    False: "Não"
})

print(df.head())