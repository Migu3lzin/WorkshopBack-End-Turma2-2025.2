"""def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)"""

try:
    def somar(a, b):
        return a + b

    resultado = somar(10, "5")
    print(resultado)
except TypeError:
    print("Erro: Não é possível somar valores com string.")    