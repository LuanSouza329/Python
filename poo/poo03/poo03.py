class Human:
    def __init__(self, name:str):
        self.__name:str = name #atributo privado!
        
    def apresentarse(self) -> None:
        pass
        
    def getName(self):
            return self.__name
        
class Pessoa(Human):
    
    def __init__(self, name, age:int):
        super().__init__(name)
        self.__setAge(age)
    
    def __setAge(self, age:int):
        if age < 0:
            print("A idade deve ser maior que 0")
            self.age = 0
        else:
            self.age = age
            
    def getAge(self):
        return self.age
        
    def apresentarse(self, mensagem:str) -> None: 
        print(mensagem)

p1 = Pessoa("Evelyn", 12)
print(p1.getAge())