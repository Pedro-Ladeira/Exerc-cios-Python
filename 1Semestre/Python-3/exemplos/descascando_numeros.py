#escreva um programa que recebe um número inteiro representando um cpf 
#e imprime cada um dos dígitos.
#Por exemplo, se cpf = 23420938107, vai aparecer na tela os seguintes números:
#7,0,1,8,3,9,0,2,4,3,2
import os 

os.system("cls")
cpf = int(input("Digite seu CPF: "))
resp = ""

'''Deste jeito exibe os números como foi pedido no exercicio,
de tras para frente e com uma virgula entre eles'''
while cpf != 0:
    dig = cpf % 10
    resp = resp + str(dig) + ", "
    cpf = cpf // 10

'''Deste jeito os números são exibidos na ordem certa!
while cpf != 0:
    dig = cpf % 10
    resp = str(dig) + resp
    cpf = cpf // 10
'''

print(resp)


