with open("dados.txt", "w") as arquivo:
    arquivo.write("Olá mundo depois do arquivo escrito")
    
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    
print(conteudo)


#Modo	Função
#"r"	leitura
#"w"	escrita
#"a"	append
#"x"	criar

#Melhor maneira de criar arquivos, pois faz a abertura e o fechamendo do arquivo e não há vazamentos
#with open("dados.txt", "r") as arquivo:
#   conteudo = arquivo.read()

