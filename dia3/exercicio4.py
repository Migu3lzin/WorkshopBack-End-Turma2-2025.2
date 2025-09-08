"""numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])"""

numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 


try:
    print(numeros[indice])
    
except IndexError:
    print("Erro: Índice fora do intervalo.")
