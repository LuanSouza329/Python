import json
import os

documento:str = "cadastroAlunos.json"

def menu () -> int:
    print('Digite uma das opções abaixo')
    
    try:
        option:str = int(input("1 - Cadastrar Alunos. \n2 - Listar Alunos.\n3 - Sair. \n").strip().title())
    except ValueError:
        print ('Por favor, Digite um número inteiro para seguir \n')
        return 0
        
    
    return option

def cadastrarAlunos (nome: str, idade: int) -> str:
    
    newUser:dict = {"nome": nome, "idade": idade}
    
    if os.path.exists(documento):
        with open(documento, 'r', encoding="utf-8") as arquivo:
            try:   
                list_user:list[dict] = json.load(arquivo)
            except ValueError:
                list_user = []
    else:
        list_user:list[dict] = []
        
    list_user.append(newUser)
    
    with open(documento, 'w', encoding="utf-8") as arquivo:
        json.dump(list_user, arquivo, indent=3,ensure_ascii=False)
    
    return f"Aluno {newUser['nome']} cadastrado com sucesso!!! \n"

def listarAlunos (documento:str) -> None: 
      if os.path.exists(documento):
        with open(documento, 'r', encoding="utf-8") as arquivo:
            lista_alunos:list[dict] = json.load(arquivo)
        
        if not lista_alunos:
            print('Lista de estudantes vazia, por favor cadastre um novo estudante. ')
        else:
            print("-----------------LISTA DE ALUNOS----------------- \n")
            for aluno in lista_alunos:
                print(f"Aluno: {aluno['nome']}, Idade: {aluno['idade']}.")
            
            print("\n")

def escola() -> None:
    while True:
        print('Seja Bem-vindo a escola Python!!! ')
        
        option = menu()
        
        if option == 1:
            while True:
                nome:str = input("Digite o nome do Aluno ou 0 para sair. \n").strip().title()
                if nome == "0":
                    break
                try: 
                    idade = int(input("Digite a idade do Aluno. \n ").strip())
                    if idade < 0:
                        print("Idade menor que 0, por favor, tente novamente \n")
                        continue
                except ValueError:
                        print("Idade deve ser um  número inteiro, tente novamente. \n")
                        
                print(cadastrarAlunos(nome, idade))
                
        elif option == 2:
            listarAlunos(documento)
        elif option == 3:
            print("Fechando o sistema da Escola... ")
            print("Volte sempre! \n")
            break
        else: 
            print("Digite uma das opções disponibilizadas no Menu. \n")
                        

            
            

escola()
