import json
import os

documento:str = "cadastroAlunos.json"

if os.path.exists(documento):
        with open(documento, 'r', encoding="utf-8") as arquivo:
            lista_alunos:list[dict] = json.load(arquivo)
            
idade = [aluno['idade'] for aluno in lista_alunos]

media = sum(idade) / len(idade)
maior = max(idade)
menor = min(idade)

print(f"A media de idade dos alunos é {media:.2f}")
print(f"A maior idade entre os alunos é {maior}")
print(f"A menor idade entre os alunos é {menor}")