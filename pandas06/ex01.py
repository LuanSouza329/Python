import pandas as pd

dados = {
    "nome": ["Ana", "Carlos", "Maria", "João"],
    "idade": [20, None, 25, None]
}

df = pd.DataFrame(dados)

soma_nulo = df.isna().sum() #Soma o número de valores nulso

idade_nula = df[df['idade'].isna()] # Retorna a tabela com True ou False em caso de valores nulos

sem_nulo = df[df['idade'].notna()] # Retorna a tabela com True ou False para valores não nulos

print(df.isna())

print(soma_nulo)
print(idade_nula)
print(sem_nulo)

media = df['idade'].mean()

df["idade"] = df['idade'].fillna(media) #Fillna preenche os valores nulos com a média da idade.

print(df, '\n\n\n')

df['idade'] = df['idade'].fillna(0)

print(df, '\n\n\n')