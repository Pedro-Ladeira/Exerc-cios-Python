cpf = int(input("Digite seu cpf: "))
valor = ""
valor2 = ""
valor3 = ""
valor4 = ""

cpf_str = str(cpf)
while len(cpf_str) != 11:
    cpf = int(input("Digite um cpf válido (com 11 números): "))

print_cpf = cpf % 100
valor = str(print_cpf) + valor
cpf = cpf // 100

print_cpf = cpf % 1000
valor2 = str(print_cpf) + valor2
cpf = cpf // 1000

print_cpf = cpf % 1000
valor3 = str(print_cpf) + valor3
cpf = cpf // 1000

print_cpf = cpf % 1000
valor4 = str(print_cpf) + valor4
cpf = cpf // 1000

print(f"{valor4}.{valor3}.{valor2}-{valor}")