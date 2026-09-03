pessoa = {
    "nome": "Luan",
    "idade": 32,
    "cidade": "São Paulo"
} # Cria um dicionário chamado "pessoa" com as chaves "nome", "idade" e "cidade" e seus respectivos valores.

print(pessoa) # Imprime o dicionário "pessoa" na tela.
print(pessoa["nome"]) # Imprime o valor associado à chave "nome" do dicionário "pessoa".
print(pessoa["idade"]) # Imprime o valor associado à chave "idade" do dicionário "pessoa".
print(pessoa["cidade"]) # Imprime o valor associado à chave "cidade" do dicionário "pessoa".

pessoa['nome'] = "Maria" # Altera o valor associado à chave "nome" do dicionário "pessoa" para "Maria".
pessoa['idade'] = 28 # Altera o valor associado à chave "idade" do dicionário "pessoa" para 28.
del pessoa['cidade'] # Remove a chave "cidade" e seu valor associado do dicionário "pessoa".
print(pessoa) # Imprime o dicionário "pessoa" na tela.

for chave in pessoa: # Itera sobre as chaves do dicionário "pessoa".
    print(chave + ": " + str(pessoa[chave])) # Imprime o valor associado a cada chave do dicionário "pessoa" na tela.

if "nome" in pessoa:
    print("Existe")

print(pessoa.get("nome")) # Retorna o valor associado à chave "nome" do dicionário "pessoa".