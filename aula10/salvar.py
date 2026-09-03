import json
import os

nome_arquivo = "usuarios.json"

# 1. Captura os novos dados do usuário pelo terminal
novo_nome = input("Digite o nome: ")
nova_idade = int(input("Digite a idade: "))
nova_cidade = input("Digite a cidade: ")

novo_usuario = {"nome": novo_nome, "idade": nova_idade, "cidade": nova_cidade}

# 2. Tenta ler o arquivo existente; se não existir, cria uma lista vazia
if os.path.exists(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        lista_usuarios = json.load(arquivo)
else:
    lista_usuarios = []

# 3. Adiciona o novo dicionário à lista
lista_usuarios.append(novo_usuario)

# 4. Salva a lista atualizada de volta no arquivo
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(lista_usuarios, arquivo, indent=4, ensure_ascii=False)

print(f"\n{novo_nome} foi adicionado com sucesso ao arquivo {nome_arquivo}!")
