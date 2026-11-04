class Human:
    def __init__(self, name:str):
        self.name:str = name
        
    def apresentarse(self) -> None:
        print()
        
class Pessoa(Human):
    
    def __init__(self, name, age:int):
        super().__init__(name)
        self.age:int = age
        
    def apresentarse(self, mensagem:str) -> None: 
        print(mensagem)

p1 = Pessoa("Evelyn", 30)

p1.apresentarse('ola')