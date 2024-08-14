# Transforme os seguintes numeros de decimal para binario:
# 238, 1043 e 4502
import os

def clear():
    os.system("cls")

clear()

num1 = 238
num2 = 1043
num3 = 4502
valor1 = ""
valor2 = ""
valor3 = ""

while num1 > 0:
    printnum = num1 % 2
    valor1 = str(printnum) + valor1
    num1 = num1 // 2

while num2 > 0:
    printnum = num2 % 2
    valor2 = str(printnum) + valor2
    num2 = num2 // 2

while num3 > 0:
    printnum = num3 % 2
    valor3 = str(printnum) + valor3
    num3 = num3 // 2

print(valor1, valor2, valor3)

