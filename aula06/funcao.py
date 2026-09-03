nome:str = "Luan de Souza"

def saudacao(nome:str):
    print(f"Olá, {nome}")
    
def sum (n1: int, n2: int) -> int:
    return n1 + n2

def isPar(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    return False

    
    
saudacao(nome) # Chama a função saudacao para exibir a mensagem de saudação.
resultado: int = sum(10, 30) # Chama a função sum para calcular a soma de 10 e 30, armazenando o resultado na variável resultado.
print(f"O Resultado da soma é: {resultado}")

res: bool = isPar(3)
if res:
    print("O número é par.")