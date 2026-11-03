class Human:
    def __init__(self, name:str) -> None:
        self.name:str = name
    
    def apresentarse(self) -> None:
        print(f"Olá, meu nome é {self.name}")

#Herança, A herança é passada da classe pai para a filho através do class()
#Para receber o construtor do pai, chamamos o super e passamos as propriedades necessárias.
#Para passar todas as propriedades para uma classe filho e sem adição de novas propriedades passamos pass para evitar erros

class Person(Human):
    def __init__(self, name:str, age:int):
        super().__init__(name)
        self.age = age
        
class Student(Person):
    pass
        
po = Human('Luan')        
p1 = Person('Luan', 33)
st1 = Student('Teste', 32)

p1.apresentarse()
st1.apresentarse()