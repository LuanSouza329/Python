import pandas as pd

df = pd.read_csv('dados_vendas.csv')

df['faturamento'] = (
    df['preco_unitario'] *
    df['quantidade']
)

df['data'] = pd.to_datetime(df['data']) # Conversão para data

df['dia_mes'] = df['data'].dt.day
df['dia_semana'] = df['data'].dt.day_name()
df['mes'] = df['data'].dt.month
df['ano'] = df['data'].dt.year

maior_faturamento = df.groupby('mes')['faturamento'].max()
dia_da_semana = df.groupby('dia_mes')['faturamento'].max()

print(df)

print(dia_da_semana.sort_values(ascending=False))
