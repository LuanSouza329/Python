import pandas as pd

df = pd.DataFrame({
    'ID_vendedor': [101, 102, 103]
})

tabela_aux = {
    101: 'Ana',
    102: 'Carlos',
    103: 'Maria'
}


df['ID_vendedor'] = df['ID_vendedor'].map(tabela_aux)

print(df)