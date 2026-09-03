lista:list = [1,2,3,4,5,6,7]

def media(lista:list) -> float:
    if len(lista) == 0:
        return 0.0
    return sum(lista) / len(lista)

print(media(lista))