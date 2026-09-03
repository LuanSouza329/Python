import pandas as pd

df = pd.read_csv('dados_vendas.csv')

df['faturamento'] = (
    df['preco_unitario'] * 
    df['quantidade']
)

relatorio = pd.pivot_table(
    df,
    index="vendedor",
    columns="produto",
    values="faturamento",
    aggfunc="sum",
    fill_value=0
)

maior_vendedor = relatorio['Notebook'].idxmax()

print(maior_vendedor)