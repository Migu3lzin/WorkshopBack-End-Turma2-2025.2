import math

class FiguraGeometrica:
    @staticmethod
    def area_circulo(raio: float) -> float:
        return math.pi * math.pow(raio, 2)
    
    @staticmethod
    def area_triangulo(base: float, altura: float) -> float:
        return (base * altura) / 2
    
    @staticmethod
    def hipotenusa(cateto1: float, cateto2: float) -> float:
        return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))
    
print(FiguraGeometrica.area_circulo(4))
print(FiguraGeometrica.area_triangulo(4, 6))
print(FiguraGeometrica.hipotenusa(3, 4))    