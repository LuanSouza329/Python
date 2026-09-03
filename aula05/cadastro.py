cadastroAlunos:list = []

aberto:bool = True


def menu():
    print("Bem-vindo ao sistema de cadastro de alunos!")
    print(
        "1 - Cadastrar aluno \n"
        "2 - Listar alunos \n"
        "3 - Buscar aluno \n"
        "4 - Sair \n"
    )
    
    userOption:int = int(input("Escolha uma opção: "))
    
    return userOption


def cadastrarAluno(cadastroAlunos:list):
        aluno:dict = {"nome": "", "idade": 0, "curso": ""}
    
        aluno["nome"] = input("Digite o nome do aluno ou 0 para sair: ").strip().title()
        if aluno["nome"] == "0":
            return
        try: aluno["idade"] = int(input("Digite a idade do aluno: \n" ))
        except ValueError:
            print("Idade inválida. Tente novamente.")
            return
        try:
            cursos = {
                1: "Ciência da Computação",
                2: "Engenharia de Software",
                3: "Análise e Desenvolvimento de Sistemas"
            }
            
            opcaoCurso:int = int(input("Escolha o curso do aluno: \n"
                "1 - Ciência da Computação \n"
                "2 - Engenharia de Software \n"
                "3 - Análise e Desenvolvimento de Sistemas \n"
            ))
            
            if opcaoCurso not in cursos:
                print("Curso inválido. Tente novamente.")
                return
            
            aluno["curso"] = cursos.get(opcaoCurso)
        except ValueError:
            print("Curso inválido. Tente novamente.")
            return
        cadastroAlunos.append(aluno)
        print(f"Aluno {aluno['nome']} cadastrado com sucesso! \n")
        
        return aluno
                
def listarAlunos(cadastroAlunos:list):
        print("Alunos cadastrados: \n")
        if not cadastroAlunos:
            print("Nenhum aluno cadastrado. \n")
        for aluno in cadastroAlunos:
            print(f"- {aluno['nome']}, {aluno['idade']} anos, curso: {aluno['curso']}")
        print()
        
def buscarAluno(nomeBusca:str):
        encontrado:bool = False
        
        for aluno in cadastroAlunos:
            if aluno["nome"] == nomeBusca:
                print(f"Aluno encontrado: {aluno['nome']}, {aluno['idade']} anos, curso: {aluno['curso']} \n")
                encontrado = True
                break
        if not encontrado:
            print(f"Aluno {nomeBusca} não encontrado. \n")
        
while aberto:
    try:
        option = menu()
    except ValueError:
        print("Opção inválida. Tente novamente.")
        continue
    
    if option == 1:
        while True:
            cadastrarAluno(cadastroAlunos)
            continuar:str = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
            if continuar != 's':
                break
    elif option == 2:
        listarAlunos(cadastroAlunos)
    elif option == 3:
        nomeBusca:str = input("Digite o nome do aluno para buscar: ").strip().title()
        buscarAluno(nomeBusca)
    elif option == 4:
        print("Saindo do sistema de cadastro de alunos... Até mais! \n")
        aberto = False
    else:
        print("Opção inválida! Tente novamente. \n")