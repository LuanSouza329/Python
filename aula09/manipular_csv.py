import csv

with open("usuarios.csv", "w", newline="") as arquivo:

    writer = csv.writer(arquivo)

    writer.writerow(["nome", "idade"])

    writer.writerow(["Ana", 20])
    

with open("usuarios.csv", 'r') as arquivo:
    leitor = csv.reader(arquivo)
    
    for ler in leitor:
        print(ler)