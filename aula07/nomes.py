usuarios = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Charlie", "idade": 35},
    {"nome": "David", "idade": 10},
    {"nome": "Eve", "idade": 27},
]

user = [u["nome"] for u in usuarios if u["idade"] > 18]
minors =  [u["nome"] for u in usuarios if u["idade"] <= 18]

print(user)
print(minors)