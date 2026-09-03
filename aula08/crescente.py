numeros:list[int] = [5, 2, 8, 1, 9]

crescente:list[int] = sorted(numeros)
decrescente:list[int] = sorted(numeros, reverse=True)

print(list(crescente))
print(list(decrescente))