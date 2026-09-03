import pandas as pd

dados = {
    "nome": ["Ana", "Carlos", "Maria", "João"],
    "idade": [20, None, 25, 30],
    "cidade": ["São Paulo", "Rio", None, "Curitiba"]
}

df = pd.DataFrame(dados)

df_limpo =  df.dropna() # Remove linhas com valores ausentes

df['idade'] = df['idade'].fillna(0) # Substitui valores ausentes na coluna 'idade' por 0

nam_resulto = df[df['cidade'].isna()] # Filtra linhas onde a coluna 'cidade' tem valores ausentes

sem_nan = df[df["cidade"].notna()] # Filtra linhas onde a coluna 'cidade' não tem valores ausentes

print(sem_nan)