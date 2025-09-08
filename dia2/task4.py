class Animal():
    def falar(self):
        return "barulho generico do animal"
    
class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"
    
    print(Cachorro.falar("Gato"))
         
