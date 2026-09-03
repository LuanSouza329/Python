pessoas = [
    {"nome": "Alice", "idade": 30, "cidade": "São Paulo"},
    {"nome": "Bob", "idade": 25, "cidade": "Rio de Janeiro"},
    {"nome": "Charlie", "idade": 35, "cidade": "Belo Horizonte"},
    {"nome": "Diana", "idade": 22, "cidade": "Curitiba"},
]

def listarPessoas(pessoas: list):
    for pessoa in pessoas:
        if pessoa["idade"] >= 25:
            print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")

listarPessoas(pessoas);