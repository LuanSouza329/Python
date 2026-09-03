produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Monitor", "preco": 1200}
]

nomes = list(map(lambda p: p["nome"], produtos))

produtos_caros = list(
    filter(
        lambda produto: produto["preco"] > 1000,
        produtos
    )
)

produtos_ordenados = sorted(
    produtos,
    key=lambda produto: produto["preco"]
)

todos_precos = list(
    map(lambda produto: produto["preco"], produtos)
)

media_precos = sum(todos_precos) / len(todos_precos)

print("----- NOMES -----")

for nome in nomes:
    print(nome)

print("\n----- PRODUTOS ACIMA DE 1000 -----")

for produto in produtos_caros:
    print(f"{produto['nome']} - R${produto['preco']}")

print("\n----- ORDENADOS -----")

for produto in produtos_ordenados:
    print(f"{produto['nome']} - R${produto['preco']}")

print(f"\nMédia dos preços: R${media_precos:.2f}")