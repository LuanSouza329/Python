numeros:list[int] = [10, 15, 20, 33, 40, 55]

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
quadrados = [num ** 2 for num in numeros]
media = sum(numeros) / len(numeros)


print("Números:", numeros)
print("Pares:", pares)
print("Ímpares:", impares)
print("Quadrados:", quadrados)
print(f"Média: {media:.2f}")