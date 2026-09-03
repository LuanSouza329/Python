numeros = []
pares = []

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))

    if numero < 0:
        print("Número negativo não é permitido. Digite um número positivo.")
        continue

    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)

print(f"Números digitados: {numeros}")
print(f"Números pares: {pares}")
