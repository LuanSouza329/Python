import pandas as pd

produtos = {
    "produto": ["Notebook", "Mouse", "Monitor", "Teclado"],
    "preco": [3500, 80, 1200, 250]
}

df = pd.DataFrame(produtos)

print('------------------PRODUTOS COM PREÇO MAIOR QUE 1000----------------------')
print(
    df[
        df['preco'] > 1000
    ]
)

print('------------------PRODUTOS COM PREÇO MAIOR QUE 1000----------------------')
print(
    df[
        df['preco'] < 1000   
    ]
)

print('----------------------PRODUTOS DESAFIO--------------------------')
print(
   df[
        df['preco'] > 1000
   ]
)
