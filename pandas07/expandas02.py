import pandas as pd

df = pd.read_csv('dados_vendas.csv')

df['faturamento'] = df['preco_unitario'] * df['quantidade']

faturamento_vendedor = df.groupby('vendedor')['faturamento'].sum()

print(faturamento_vendedor.sort_values(ascending=False))
