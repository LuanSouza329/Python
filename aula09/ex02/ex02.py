import csv

def ler_alunos(documento):
    with open(documento, 'r') as arquivo:
        leitor = csv.reader(arquivo)

        print('---------------ALUNOS EM BANCO DE DADOS (ETL - Básico)  ------------------')
        
        for aluno in leitor:
            print(f"Nome: {aluno[0]} | Idade: {aluno[1]}")
            
def idade_alunos(documento):
    with open(documento, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        
        idades = list(
            map(lambda alunos: int(alunos[1]), leitor)
        )
        return idades
    
def cadastrar_alunos(documento, nome, idade):
    with open(documento, 'a', newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, idade])
            
aberto:bool = True

while aberto:
    nome:str = input('Digite seu nome ou 0 para sair: ').strip().title()
    if nome == '0':
        break
    try: idade:int = int(input('Digite a sua idade: ').strip())
    except ValueError: 
        print('Valor incorreto, por favor digite um número inteiro: ')
        continue
    
    if idade < 0:
        print("Idade incorreta, por favor digite um valor válido: ")
        continue
    cadastrar_alunos('alunos.csv', nome, idade)
        
ler_alunos('alunos.csv')

idades = idade_alunos('alunos.csv')

media = sum(idades) / len(idades)

print(f"A média de idade dos alunos é: {media} ")
        