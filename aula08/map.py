numeros:list[int] = [1, 2, 3, 4, 5]

resultado = map(lambda x: x * 2, numeros)

for res in resultado:
    print(res)
    
#Map é uma função que recebe uma função e um iterável, e retorna um iterador que aplica a função a cada item do iterável.
#No exemplo acima, a função lambda x: x * 2 é aplicada a cada número na lista numeros, resultando em uma nova lista onde cada número é multiplicado por 2.