pessoa = {"nome": "", "sobrenome": "", "idade": 0}

def criar_pessoa(nome, sobrenome, idade):
    pessoa["nome"] = nome
    pessoa["sobrenome"] = sobrenome
    pessoa["idade"] = idade
    return pessoa

input_nome = input("Digite o nome: ")
input_sobrenome = input("Digite o sobrenome: ")
input_idade = int(input("Digite a idade: "))

pessoa_criada = criar_pessoa(input_nome, input_sobrenome, input_idade)

print(f"Pessoa criada: {pessoa_criada['idade']} anos, {pessoa_criada['nome']} {pessoa_criada['sobrenome']}")
