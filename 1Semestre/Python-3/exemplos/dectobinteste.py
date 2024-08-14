import os
def clear():
    os.system("cls")
clear()

decimal = int(input("digite um número: "))
resultado = ""

while decimal > 0:
    resto = decimal % 2
    resultado = str(resto) + resultado
    decimal = decimal // 2

print(f"Seu número em binário é: {resultado}")  