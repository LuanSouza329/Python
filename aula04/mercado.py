mercado = []

aberto = True

while aberto: 
    print("Bem-vindo ao mercado! ")
    print("Escolha uma das opções abaixo: \n ")

    try:
        options = int(
            input(
                "1 - Adicionar produto \n"
                "2 - Remover produto \n"
                "3 - Listar produtos \n"
                "4 - Sair \n"
            )
        )
    except ValueError:
        print("Digite apenas os números definidos nas opções.")
        continue

    if options == 1:
        while True:
            produto = input("Digite o nome do produto: ou '0' para parar: ").strip().title()
            if produto == "0":
                break
            mercado.append(produto)
            print(f"{produto} adicionado ao mercado! \n")
    elif options == 2:
        produto = input("Digite o nome do produto: ").strip().title()
        if  produto in mercado:
            mercado.remove(produto)
            print(f"{produto} removido do mercado! \n")
        else:
            print(f"{produto} não encontrado no mercado! \n")
    elif options == 3:
        print("Produtos no mercado: ")
        for produto in mercado:
            print(f"- {produto}")
        print()
    elif options == 4:
        print("Saindo do mercado... Até mais! \n")
        aberto = False
    else:
        print("Opção inválida! Tente novamente. \n")
