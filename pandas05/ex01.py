import pandas as pd

clientes = pd.DataFrame({
    "id_cliente": [1,2,3],
    "nome": ["João", "Maria", "Joana"]
})

pedidos = pd.DataFrame({
    "id_cliente": [1,1,1,2],
    "valor": [100, 200, 300, 400]
})

vendas = pd.merge(
    clientes,
    pedidos,
    on="id_cliente",
    how="left"
)

print(vendas)

totalJoao = vendas.groupby("nome")["valor"].sum().loc['João']
totalJoana = vendas.groupby("nome")["valor"].sum().loc['Joana']
totalMaria = vendas.groupby("nome")["valor"].sum().loc['Maria']


print(totalJoao)
print(totalJoana)
print(totalMaria)

maior_valor = vendas.groupby("nome")["valor"].sum().idxmax()
print(maior_valor)