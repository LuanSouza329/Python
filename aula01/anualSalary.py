name = input("Digite seu nome: ");
salary = float(input("Digite seu salário: "));

annual_salary = salary * 12;

print(f"Olá, {name}! Seu salário anual é: R$ {annual_salary:.2f} e com decimo terceiro salário é: R$ {annual_salary + salary:.2f}");