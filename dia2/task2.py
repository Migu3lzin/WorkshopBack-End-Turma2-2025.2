import math 

def arredondamentos(mumero: float) -> dict:
     return {
          "piso": math.floor(mumero),
          "teto": math.ceil(mumero),
          "arredondado": round(mumero)
     }
arredondamentos(5.3)

print(arredondamentos(5.3))
