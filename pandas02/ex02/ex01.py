import pandas as pd

dados = {
    "nome": ["Ana", "Carlos", "Maria", "João", "Pedro"],
    "idade": [20, 30, 17, 40, 15]
}

df = pd.DataFrame(dados)


print("------------------ALUNOS MAIOR QUE 18 ANOS----------------------")
print(
    df[
        df['idade'] > 18
    ]
)

print("------------------ALUNOS MENORES QUE 18 ANOS----------------------")
print(
    df[
        df["idade"] < 18
    ]
)

print("------------------ALUNOS ENTRE 18 E 30 ANOS----------------------")
print(
    df[
        (df['idade'] > 18) 
        & (df['idade'] < 30)
    ]
)