import pandas as pd

clientes = pd.DataFrame({
    "id_cliente": [1, 2, 3, 4],
    "nome": ["João", "Maria", "Carlos", "Ana"]
})

vendas = pd.DataFrame({
    "id_cliente": [1, 1, 2, 3, 5],
    "valor": [500, 300, 800, 200, 1000]
})

df =  pd.merge(
    clientes,
    vendas,
    on="id_cliente",
    how="outer"
)


print(df.isna())

