boleto = int(input("Informe o numero do boleto: "))
soma = 0
mult = 2

while boleto != 0:
    digito = boleto % 10
    boleto = boleto // 10

print(digito)
