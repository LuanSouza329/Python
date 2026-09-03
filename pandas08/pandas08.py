import pandas as pd

df = pd.read_csv("dados_vendas.csv")

df['faturamento'] = df['preco_unitario'] * df['quantidade']

relatorio = (
    df
    .groupby('vendedor')
    .agg({ #agg significa agregar, neste tipo de consulta, podemos consultar muitas metricas de uma vez
        "faturamento":[
            "sum",
            "mean",
            "min",
            "max"
        ]
    })
)

relatorio2 = (
    df
    .groupby('vendedor')
    .agg( #Aqui nos permite nomear as colunas
        faturamento_total = ('faturamento', 'sum'),
        quantidade_total = ('quantidade', 'sum'),
        ticket_medio = ('faturamento', 'mean'),
        maior_venda = ('faturamento', 'max')
    )
)

print(relatorio2)