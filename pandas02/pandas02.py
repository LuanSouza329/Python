import pandas as pd

dados = {
    "nome": ["Ana", "Carlos", "Maria", "João", "Carlos"],
    "idade": [20, 30, 17, 40, 25]
}

df = pd.DataFrame(dados)

print(df[df['idade'] > 18], "\n")

print("----------------- MENORES --------------------")

print(df[df['idade'] < 18])

print("----------------- IGUAL A --------------------")

print(df[df['nome'] == 'Carlos'])

print("----------------- DIFERENTE DE --------------------")
print(df[df['nome'] != 'Calos'])

print("----------------- 2 CONDIÇÕES E --------------------")
print(df[(df['idade'] > 18) 
        & (df['idade'] < 30)])

print("----------------- 2 CONDIÇÕES OU --------------------")
print( df[
    (df["idade"] < 18)
    | (df["idade"] > 35)
]
)