temperartura = input("Digite a temperatura em Celsius: ");

if temperartura.__contains__(","):
    temperartura = float(temperartura.replace(",", "."));

temperartura = float(temperartura);

fahrenheit = (temperartura * 9/5) + 32;

print(f"A temperatura em Fahrenheit é: {fahrenheit}");