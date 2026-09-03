usuarios:list[dict] = [
    {"nome": "Ana", "idade": 20},
    {"nome": "Carlos", "idade": 15},
    {"nome": "Maria", "idade": 32}
]

userAge:list[dict] = sorted(usuarios, key=lambda user: user["idade"])
userAgeReverse:list[dict] = sorted(usuarios, key = lambda user: user["idade"], reverse=True)

for user in userAge:
    print(f"{user['nome']} - {user['idade']} anos")

print("----------------Reverse-----------------")

for user in userAgeReverse:
    print(f"{user['nome']} - {user['idade']} anos")