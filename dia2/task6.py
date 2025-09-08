class Animal():
    def falar(self):
        return "barulho generico do animal"
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos"
        
    
class Cachorro(Animal):
    def falar(self):
        return "Au au!"
    def __init__(self, nome, idade):
        super().__init__(nome,idade)

class Gato(Animal):
    def falar(self):
        return "Miau!"
    def __init__(self, nome, idade):
        super().__init__(nome,idade)

pingo = Cachorro = Cachorro("pingo", 7)
print(pingo.apresentar())

francisco = Gato = Gato("francisco", 3)
print(francisco.apresentar())
        

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        return [f"{a.apresentar()} faz: {a.falar()}" for a in self.animais]
    
        def filtar_por_tipo(self, tipo):
            return [a for a in self.animais if isinstance(a, tipo)]
        
        
    
