import pandas as pd

df = pd.read_csv('dados.csv')

#Cálculo do lucro unitário, lucro da venda e lucro total
df['lucro_unitario'] = (
    df['preco_unitario'] - 
    df['custo_unitario']
)

#Cálculo faturamento
df['faturamento'] = (
    df['preco_unitario'] *
    df['quantidade']
)

df['margem_lucro'] = (
    (df['lucro_unitario'] / 
     df['preco_unitario']) * 100
).round(0)

#Cálculo do lucro total
df['lucro_total'] = (
    (df['preco_unitario'] - 
    df['custo_unitario']) *
    df['quantidade']
)

def classificar_margem (valor):
    if(valor > 40):
        return "Alta"
    
    elif(valor > 25 and valor < 39):
        return "Média"
    else:
        return "Baixa"

#Função de classificar do valor de faturamento
def classificar(valor):
    if(valor < 500):
        return "Pequeno"
    
    elif(valor > 501 and valor < 3000):
        return "Médio"
    
    else:
        return "Grande"
        
def classificacao_clientes(valor):
    if(valor > 8000):
        return "VIP"
    
    else:
        return "Comum"        
        
#Coluna de classificação usando a função apply para aplicar a função criada    
df['classificacao'] = (
    df['faturamento'].apply(classificar)
)

#Coluna de classificação de margem
df['margem_classificada'] = (
    df['margem_lucro'].apply(classificar_margem)
)

relatorio = df.groupby('cliente').agg(
    faturamento = ('faturamento', 'sum'),
    lucro = ("lucro_total", 'sum')
)

relatorio['categoria_cliente'] = (
    df.groupby('cliente')['faturamento'].sum().apply(classificacao_clientes)
)

print(df.head(), '\n\n\n')

print(relatorio, '\n\n\n')

total_vip = len(relatorio[relatorio['categoria_cliente']=="VIP"])

faturamento_medio_categoria_cliente = relatorio.groupby('categoria_cliente')['faturamento'].mean().round(2)

tbl_faturamento_total_vip = relatorio.groupby('categoria_cliente')['faturamento'].sum()

media_vip = faturamento_medio_categoria_cliente['VIP']

faturamento_total_vip = tbl_faturamento_total_vip['VIP']

conclusao = (f" Existem {total_vip} clientes Vip. \n O lucro médio dos clientes Vip é de {media_vip}. \n O faturamento total obtido pelos clientes VIP é {faturamento_total_vip}")

print(conclusao)