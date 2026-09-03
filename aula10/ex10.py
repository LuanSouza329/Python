import json

pessoa:dict = {
    "nome": "Luan",
    "idade": 32
}

string_json = json.dumps(pessoa) #String para Json

dados = json.loads(string_json) #Json para string

print(pessoa)