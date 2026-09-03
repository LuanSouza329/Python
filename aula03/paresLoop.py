acumulador = 0

for i in range(51):
    if i % 2 == 0:
        acumulador += 1

print(f"Existem {acumulador} números pares entre 0 e 50.")