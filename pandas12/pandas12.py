#Importar pandas
import pandas as pd

#leitura do CSV
df = pd.read_csv('dados.csv')

#Transformar a coluna data em datacase
df['data'] = pd.to_datetime(df['data'])

#Adição das colunas de dia, mes e ano
df['dia_mes'] = df['data'].dt.day
df['dia_semana'] = df['data'].dt.day_name()
df['mes'] = df['data'].dt.month_name()
df['ano'] = df['data'].dt.year


#Cálculo do lucro unitário, lucro da venda e lucro total
df['lucro_unitario'] = (
    df['preco_unitario'] - 
    df['custo_unitario']
)

#Cálculo do lucro da venda e lucro total
df['lucro_venda'] = (
    df['lucro_unitario'] * 
    df['quantidade']
)

#Cálculo do lucro total
df['lucro_total'] = (
    (df['preco_unitario'] - 
    df['custo_unitario']) *
    df['quantidade']
)

#Cálculo do lucro total e do vendedor com mais lucro
lucro_total = df['lucro_total'].sum()

#Cálculos dos vendedores com mais lucro
tbl_mais_lucro = df.groupby('vendedor')['lucro_total'].sum()

#Nome vendedor com mais lucro
nome_vendedor_com_mais_lucro = tbl_mais_lucro.idxmax()

#Valor do vendedor com mais lucro
vendedor_com_mais_lucro = tbl_mais_lucro.max()

#Cálculo do produto com mais lucro
tbl_produto_mais_lucro = df.groupby('produto')['lucro_total'].sum()

#Nome do produto com mais lucro
nome_produto_mais_lucro = tbl_produto_mais_lucro.idxmax()

#Valor do produto com mais lucro
produto_mais_lucro = tbl_produto_mais_lucro.max()

#Cálculo da margem de lucro
df['margem_lucro'] = (
    (df['lucro_unitario'] / 
     df['preco_unitario']) * 100
).round(2)

#Cálculo da margem de lucro por categoria
tbl_margem_lucro = df.groupby('categoria')['margem_lucro'].max()

#maior margem de lucro por categoria
maior_margem_lucro_categoria = tbl_margem_lucro.idxmax()

#Calculo maior número de compras por cliente
tbl_compras_por_cliente = df.groupby('cliente')['quantidade'].sum()

#Nome do cliente com mais compras
nome_cliente_mais_compras = tbl_compras_por_cliente.idxmax()

#Valor do cliente com mais compras
cliente_mais_compras = tbl_compras_por_cliente.max()

#Cálculo de faturamento
df['faturamento'] = (
    df['preco_unitario'] * 
    df['quantidade']
)

#Cliente com maior faturamento
tbl_faturamento_por_cliente = df.groupby('cliente')['faturamento'].sum()

#Nome do cliente com maior faturamento
nome_cliente_mais_faturamento = tbl_faturamento_por_cliente.idxmax()

#Valor do cliente com maior faturamento
cliente_mais_faturamento = tbl_faturamento_por_cliente.max()

relatorio_final_cliente = df.groupby('cliente').agg(
    compras = ('quantidade', 'sum'),
    faturamento = ('faturamento', 'sum'),
    lucro = ('lucro_total', 'sum')
)

print(df, '\n\n')

print('---------ANÁLISE DE DADOS---------\n')

print(f'O lucro total da empresa foi de R$ {lucro_total:.2f}. ')
print(f'O vendedor que gerou o maior lucro foi {nome_vendedor_com_mais_lucro} com um lucro de R$ {vendedor_com_mais_lucro:.2f}.')
print(f'O produto com mais lucro foi {nome_produto_mais_lucro} com um lucro de R$ {produto_mais_lucro:.2f}.')
print(f'A categoria com maior margem de lucro foi {maior_margem_lucro_categoria} com uma margem de {tbl_margem_lucro.max():.2f}%.')
print(f'O cliente que mais comprou foi {nome_cliente_mais_compras} com um total de {cliente_mais_compras} compras.')
print(f'O cliente que mais faturou foi {nome_cliente_mais_faturamento} com um faturamento de R$ {cliente_mais_faturamento:.2f}.')

print('\n---------TABELAS DE DADOS---------\n')
print(relatorio_final_cliente, '\n\n')

conclusao = f" No período analisado, a empresa obteve um lucro total de R$ {lucro_total:.2f}. O vendedor que mais contribuiu para esse resultado foi {nome_vendedor_com_mais_lucro}, gerando um lucro de R$ {vendedor_com_mais_lucro:.2f}. \n O produto que apresentou o maior lucro foi {nome_produto_mais_lucro}, com um lucro de R$ {produto_mais_lucro:.2f}.\n A categoria com a maior margem de lucro foi {maior_margem_lucro_categoria}, alcançando uma margem de {tbl_margem_lucro.max():.2f}%. \n O cliente que realizou o maior número de compras foi {nome_cliente_mais_compras}, totalizando {cliente_mais_compras} compras, enquanto o cliente que mais faturou foi {nome_cliente_mais_faturamento}, com um faturamento de R$ {cliente_mais_faturamento:.2f}."

print('\n---------CONCLUSÃO---------\n')

print(conclusao, "\n\n")