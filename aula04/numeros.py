numeros = []

while True:
    n = int(input("Digite um número inteiro ou 0 para sair: "))
    if n == 0:
        break
    numeros.append(n)

print(f"O Maior número é: {max(numeros)}")
print(f"O Menor número é: {min(numeros)}")
print(f"A Média dos números é: {sum(numeros) / len(numeros)}")

numeros.sort()

print(f"Os números em ordem crescente são: {numeros}")