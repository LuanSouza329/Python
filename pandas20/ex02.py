import pandas as pd

df = pd.read_csv('dados.csv')

#Análise exploratória dos dados
print(df.head())
print(df.shape, '\n\n')
print(df.info(), '\n\n')
print(df.isna().sum(),'\n\n')
print(df.describe(), '\n\n')

#Respostas exercícios
print('Número total de vendedores',df['vendedor'].nunique(), '\n')
print('Quais vendedores existes', df['vendedor'].unique(), '\n')
print('Quantas vendas cada vendedor possui', df['vendedor'].value_counts(), '\n')
print('Produto que aparece mais vezes', df['produto'].value_counts().idxmax(), '\n')
print('Quantas cidades existem', df['cidade'].nunique(), '\n')
print('Quais cidades possui mais registro', df['cidade'].value_counts().idxmax())
print(
    f"Qual percentual das vendas pertence à cidade com maior número de registros: "
    f"{df['cidade'].value_counts(normalize=True).mul(100).round(2).max():.2f}%"
)