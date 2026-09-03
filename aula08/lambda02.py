numeros:list[int] = [1,2,10,25,5, -1, 12]

resultado:list[int] = list(filter(lambda valor: valor > 10, numeros))

print(resultado)