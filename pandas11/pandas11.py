import pandas as pd

df = pd.read_csv('dados_vendas.csv')

df['faturamento'] = (df['preco_unitario'] * df['quantidade'])

df['data'] = pd.to_datetime(df['data']) # Conversão para data

df['dia_mes'] = df['data'].dt.day
df['dia_semana'] = df['data'].dt.day_name()
df['mes'] = df['data'].dt.month_name()
df['ano'] = df['data'].dt.year

faturamento_total = df['faturamento'].sum();

vendedor_com_mais_faturamento = (
    df.groupby('vendedor')['faturamento']
    .sum()
    .idxmax()
)


cidade_maior_faturamento = (
    df.groupby('cidade')['faturamento']
    .sum()
    .idxmax()
)

produto_maior_faturamento = (
    df.groupby('produto')['faturamento']
    .sum()
    .idxmax()
)

categoria_maior_faturamento = (
    df.groupby('categoria')['faturamento']
    .sum()
    .idxmax()
)

maior_quantidade_vendida = (
    df.groupby('produto')['quantidade']
    .sum()
    .idxmax()
)

ticket_medio = (
    df['faturamento'].sum() / 
    df['quantidade'].sum()
)

ticket_medio_vendedor = (
    df.groupby('vendedor')['faturamento']
    .sum() / 
    df.groupby('vendedor')['quantidade']
    .sum()
)

mes_maior_faturamento = (
    df.groupby('mes')['faturamento']
    .sum()
    .idxmax()
)

relatorio_final = df.groupby('vendedor').agg({
    'faturamento': 'sum',
    'quantidade': 'sum',
})


relatorio_final['ticket_medio'] = (
    relatorio_final['faturamento'] /
    relatorio_final['quantidade']
)


print(f"A cidade de {cidade_maior_faturamento} concetrou o maior faturamento.")
print(f"O vendedor (a) {vendedor_com_mais_faturamento} aprensentou o maior faturamento.")
print(f"O produto com o maior faturamento obtido foi {produto_maior_faturamento}.")
print(f"O faturamento total é R$ {faturamento_total:.2f}")
print(f"A categoria {categoria_maior_faturamento} obteve o maior faturamento.")
print(f"O produto com a maior quantidade vendida foi {maior_quantidade_vendida}.")
print(f"O ticket médio é R$ {ticket_medio:.2f}.")
print(f"O mês com o maior faturamento é {mes_maior_faturamento}. \n")
print(f"O ticket médio por vendedor é: {ticket_medio_vendedor}. \n")


for vendedor, ticket in ticket_medio_vendedor.items():
    print(f"  {vendedor}: R$ {ticket:.2f}.")
    

print(relatorio_final)