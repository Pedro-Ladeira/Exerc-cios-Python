salario = float(input("informe o salario de joao: "))
aumento = float(input("informe o novo salario do joao apos o aumento: "))

porcentual = aumento / salario -1
novoporcentual = porcentual *100

print(f"o porcentual de aumento é de {novoporcentual}%")