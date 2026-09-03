valor01 = int(input("Digite o primeiro valor: "));

valor02 = int(input("Digite o segundo valor: "));



soma = valor01 + valor02;
subtracao = valor01 - valor02;
multiplicacao = valor01 * valor02;
divisao = valor01 / valor02;

divisao = round(divisao, 2);

print(f"A soma dos valores é: {soma}");
print(f"A subtração dos valores é: {subtracao}");
print(f"A multiplicação dos valores é: {multiplicacao}");
print(f"A divisão dos valores é: {divisao}");