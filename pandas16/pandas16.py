import pandas as pd

dados = {
    "id_cliente": [1, 2, 1, 3, 4],
    "nome": ["Ana", "Carlos", "Ana", "João", "Carlos"],
    "idade": [20, 30, 20, 40, 25],
    "valor": [500, 200, 500, 300, 400],
    "cidade": ["São Paulo", "Rio de Janeiro", "São Paulo", "Belo Horizonte", "Manaus"]
}

df = pd.DataFrame(dados)

#df.duplicated() = Retorna uma lista de bool com as linhas duplicadas.

duplicadas = df[df.duplicated()] #Retorna os registros duplicados.

#df.duplicated().sum() retorna o número de duplicadas.

df = df.drop_duplicates()

print(df.count())