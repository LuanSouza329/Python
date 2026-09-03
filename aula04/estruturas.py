nomes = ["Alice", "Bob", "Charlie"]

nomes.remove("Bob") # Remove "Bob" da lista
nomes.append("David") # Adiciona "David" ao final da lista
nomes.insert(0, "Eve") # Insere "Eve" no início da lista (índice 0)
nomes[2] = "Charlie Brown" # Modifica o elemento no índice 2 para "Charlie Brown"
nomes.sort() # Ordena a lista em ordem alfabética
nomes.reverse() # Inverte a ordem da lista
nomes.clear() # Limpa todos os elementos da lista

print(len(nomes)) # Imprime o comprimento da lista

for nome in nomes:
    print(nome) # Imprime cada nome na lista (neste caso, a lista está vazia)