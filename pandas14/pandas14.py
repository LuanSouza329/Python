import pandas as pd

df = pd.read_csv('dados.csv')

df['faturamento'] = (
    df['preco_unitario'] *
    df['quantidade']
)

abreviacao = {
    'São Paulo': 'SP',
    'Rio de Janeiro': 'RJ',
    'Belo Horizonte': 'BH',
    'Curitiba': 'CWB'
    
}

df['abreviacao'] = (
    df['cidade'].map(abreviacao)
)

print(df.head())

#O map() é utilizado para substituir ou traduzir valores de uma única coluna a partir de uma correspondência conhecida, normalmente usando um dicionário ou outra Series. Já o apply() é utilizado quando preciso executar uma lógica personalizada sobre cada elemento ou linha, como classificações, cálculos condicionais ou transformações que não podem ser representadas por uma simples correspondência.