import pandas as pd

df = pd.read_csv('dados.csv')

df['faturamento'] = (
    df['preco_unitario'] *
    df['quantidade']
)

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


produtos_caros = df.query(
    'faturamento > 4000'
)

produtos_cidade_sp = df.query(
    "categoria == 'Informática' and cidade == 'São Paulo'"
)

quantidade_maior_que_dois = df.query (
    'quantidade > 2 and faturamento > 3000'
)

cidades:list = [
    "São Paulo",
    "Rio de Janeiro"
]

cidades_ = df.query(
    'cidade in @cidades'
)

desafio = df.query(
    " categoria == 'Informática' and cidade == 'São Paulo' and lucro_venda > 1500 "
)

print(cidades_)
print(produtos_caros)
print(produtos_cidade_sp)
print(quantidade_maior_que_dois)
print(desafio)
