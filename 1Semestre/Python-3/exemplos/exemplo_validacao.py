consumo = float(input("informe o consumo"))

while consumo < 0:
    print("Valor inválido")
    consumo = float(input("Informe o valor do consumo no mês: "))

print("Você finalmente digitou um valor válido!")