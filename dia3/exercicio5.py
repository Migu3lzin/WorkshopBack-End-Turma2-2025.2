"""def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")"""

def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

try:
    resultado = dividir(int(num1), int(num2))
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.") 
except ValueError:
    print("Erro: Entrada inválida. Por favor, não insira letra só números.")