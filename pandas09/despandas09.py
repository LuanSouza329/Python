import pandas as pd

df = pd.read_csv('dados_vendas.csv')


df['faturamento'] = (
    df['preco_unitario'] * 
    df['quantidade']
)

pivot = pd.pivot_table( #Transformação em uma tabela dinâmica
    df,
    index="vendedor",
    columns="produto",
    values="faturamento",
    aggfunc="sum",
    fill_value=0
)

pivot['total'] = pivot.sum(axis=1)

print(pivot)