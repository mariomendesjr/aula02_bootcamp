# Exemplo que caus type error

try:
    resultado = len(3)
    print(resultado)

except TypeError as e:
    print(e)
else:
    print("tudo correu bem")
finally:
    print("o importante é participar")


numero = int(input("Insira um numeros: "))
if isinstance(numero, int):
    print("A variável é um inteiro")
else:
    print("A variável não é um inteiro")
