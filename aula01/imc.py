altura = float(
    input("Digite a altura da pessoa em metros: ")
    .replace(",", ".")
);

peso = float(
    input("Digite o peso da pessoa em kg: ")
    .replace(",", ".")
);

imc = peso / (altura ** 2);

print(f"O IMC da pessoa é: {imc:.2f}");
    