import pandas as pd

clientes = pd.DataFrame({
    "id_cliente": [1, 2, 3],
    "nome": ["Ana", "Carlos", "Maria"]
})

vendas = pd.DataFrame({
    "id_cliente": [1, 2, 1],
    "valor": [100, 200, 150],
    "data":['23/02/2024', '21/12/2026', '13/02/2023']
})

df = pd.merge(
    clientes, 
    vendas, 
    on="id_cliente",
    how="inner"
)

#Select clientes.id_cliente, clientes.nome vendas.id_cliente, vendas.valor from clientes left join vendas on clientes.id_cliente = vendas.id_cliente

print(df['data'])