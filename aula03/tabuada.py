
print("--------BEM VINDO À TABUADA!--------");

response = "S"

while response == "S":
    number = int(input("Digite um número para ver a tabuada: "));

    if number <= 0:
        print("Por favor, digite um número positivo.");
        continue;

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}");
    
    response = input("Deseja ver a tabuada de outro número? (S/N): ").upper();

print("Obrigado por usar a tabuada! Até a próxima!");