import pandas as pd

df = pd.read_csv('dados_vendas.csv')

df['faturamento'] = df['preco_unitario'] * df['quantidade']

relatorio = (
    df
    .groupby('vendedor')
    .agg(
        faturamento_total=("faturamento", "sum"),
        quantidade_total_vendas=("quantidade", "sum"),
        ticket_medio=("faturamento", "mean"),
        maior_venda=("faturamento", "max"),
        menor_venda = ("faturamento", 'min')
    )
)

ralatorio = relatorio.sort_values(
    'faturamento_total',
    ascending=False
)

print(relatorio.head(3))