import pandas as pd

df = pd.read_csv('dados_vendas.csv')

df['faturamento'] = df['preco_unitario'] * df['quantidade']

print(df, '\n')

faturamento_total = df['faturamento'].sum()

print(f'O faturamento total da empresa foi: {faturamento_total}')

maior_faturamento = df['faturamento'].idxmax()

print(df.loc[maior_faturamento], "\n")

menor_faturamento = df['faturamento'].idxmin()

print(df.loc[menor_faturamento], "\n")

