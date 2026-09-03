import pandas as pd

df = pd.read_csv("dados_vendas.csv")

print(df.head(5))
print(df.tail(5))
print(df.shape)
df.info() # Tem print incluído
print(df.isnull().sum()) # a comunidade usa isna() - faz a mesma coisa
print(df.describe()) # Descreve de forma estatística descritiva