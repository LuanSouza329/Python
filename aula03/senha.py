senha = "python123"

while True:

    tentativa = input("Digite a senha: ").strip().lower()

    if tentativa == senha:
        print("Acesso liberado!")
        break

    print("Senha incorreta! Tente novamente.")