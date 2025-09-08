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
        