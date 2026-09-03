salary = float (
    input("Digite o salário: ")
    .replace(",", ".")
)

if salary < 0:
    print("Salário inválido.")

if salary <= 1850:
    print("Isento de imposto.")
elif salary >= 1850 and salary < 3700:
    print("Imposto de 7,5%.")
elif salary >= 3700 and salary < 7500:
    print("Imposto de 15%.")