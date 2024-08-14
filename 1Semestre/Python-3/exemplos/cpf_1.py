import os
os.system("cls")

cpf = int(input("Digite o cpf: "))
valor = ""
valor1 = ""
valor2 = ""
valor3 = ""

print_cpf = cpf % 100
valor = str(print_cpf) + valor
cpf = cpf // 100

print_cpf = cpf % 1000
valor1 = str(print_cpf) + valor1
cpf = cpf // 1000

print_cpf = cpf % 1000
valor2 = str(print_cpf) + valor2
cpf = cpf // 1000

print_cpf = cpf % 1000
valor3 = str(print_cpf) + valor3
cpf = cpf // 1000
    
print(f"{valor3}.{valor2}.{valor1}-{valor}")