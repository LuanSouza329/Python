import json
import os

nome_arquivo = "alunos.json"

nome:str = input("Digite o nome do Aluno: ")

try: 
    idade:int =  int(input("Digite a sua idade: "))
    if(idade < 0):
        print("Idade inválida. Tente novamente. ")
        exit()
except ValueError:
    print("Idade inválida, por favor digite um número inteiro. ")
    exit()

new_user:dict = {"nome": nome, "idade": idade}

if os.path.exists(nome_arquivo):
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        lista_users:list[dict] = json.load(arquivo)
else:
    lista_users:list[dict] = []

lista_users.append(new_user)

with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
    json.dump(lista_users, arquivo, indent=4, ensure_ascii=False)

print(f"Aluno {new_user['nome']} cadastrado com sucesso!!! ")

with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
    conteudo = json.load(arquivo)
    
    print("-------------ALUNOS CADASTRADOS--------------")
for alunos in conteudo:
    print(f"Nome: {alunos['nome']}, idade: {alunos['idade']}.")
