class Pessoa:
    def __init__(self, nome:str, idade: int):
        self.nome:str = nome
        self.idade:int = idade
        self.apresentarse()
        self.mochila:list = []
    
    def getNome(self) -> str:
        return self.nome
    
    def apresentarse(self) -> None:
        print(f"Olá, meu nome é {self.nome} e minha idade é {self.idade}.")
    
    def adicionarItem(self, item: str) -> None:
        self.mochila.append(item)
        
    def mostrarItem(self) -> any:
        for itens in self.mochila:
            print(itens)

p1 = Pessoa('Luan', 33)

p1.adicionarItem('Caderno')
p1.adicionarItem('Lápis')

p1.mostrarItem()