nomes:list[str] = ["Alice", "Bob", "Charlie", "David"]

upperCase = [nome.upper() for nome in nomes] # List comprehension para criar uma nova lista com os nomes em maiúsculas

print(upperCase)

#list comprehension é uma maneira concisa de criar listas em Python. 
#Ela permite que você crie uma nova lista aplicando uma expressão a cada item de um iterável, opcionalmente filtrando os itens usando uma condição. A sintaxe geral é:
#new_list = [expression for item in iterable if condition]
#Seu uso é melhor para uma grande quantidade de itens, pois é mais eficiente do que usar um loop for tradicional para criar uma nova lista.