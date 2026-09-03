alunos: list = [
    {"nome": "João", "idade": 20},
    {"nome": "Maria", "idade": 25},
    {"nome": "Pedro", "idade": 30},
    {"nome": "Ana", "idade": 15},
    {"nome": "Lucas", "idade": 18},
    {"nome": "Carla", "idade": 12}
]

def filtrar_adultos(alunos: list) -> list:
    adultos: list = []
    for aluno in alunos:
        if aluno["idade"] >= 18:
            adultos.append(aluno)
    return adultos

adultos: list = filtrar_adultos(alunos)

print("Alunos adultos:")
for adulto in adultos:
    print(f"{adulto['nome']} - {adulto['idade']} anos")