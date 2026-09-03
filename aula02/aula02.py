age = int(
    input("Digite a sua idade: ")
)

if age < 0:
    print("Idade inválida.")

if age < 18: 
    print("Você é menor de idade.")
elif age >= 18 and age < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")