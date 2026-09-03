import pandas as pd

dados = {
    "nome": ['Ana', 'Carlos', 'Maria'],
    "idade": [20, 40, 60]
}

df = pd.DataFrame(dados)

print(df['nome']) # Imprime a série do Dataframe - Coluna nome

