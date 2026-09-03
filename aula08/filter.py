numeros:list[int] = [1, 2, 3, 4, 5]

pares = filter(lambda x: x % 2 == 0, numeros)
dobro = map(lambda x: x * 2, numeros)
reverso = sorted(numeros, reverse=True)

print(list(reverso))
print(list(pares))
print(list(dobro))
#Filter é uma função que recebe uma função e um iterável, e retorna um iterador que inclui apenas os itens do iterável para os quais a função retorna True.
#No exemplo acima, a função lambda x: x % 2 == 0 é aplicada