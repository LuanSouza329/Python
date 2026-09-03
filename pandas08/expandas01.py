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
        maior_venda=("faturamento", "max")
    )
)

print(relatorio, '\n\n')

relatorio2 = relatorio.sort_values('faturamento_total', ascending=False)

print(relatorio2)

print(
    f'O maior ticker médio é o de {relatorio2['ticket_medio'].idxmax()}.'
)
