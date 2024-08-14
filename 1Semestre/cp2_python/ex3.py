cedula = int(input("Digite o valor da cédula: "))
moeda_a = int(input("Digite o valor de uma moeda: "))
moeda_b = int(input("Digite o valor da outra moeda: "))
troca_possivel = None

for c in range(cedula // moeda_a + 1):
    for j in range(cedula // moeda_b + 1):
        if c * moeda_a + j * moeda_b == cedula:
            quantidade_a = c
            quantidade_b = j
            troca_possivel = True

if troca_possivel:
    print(f"Possível: {quantidade_a} moeda(s) de {moeda_a} e {quantidade_b} moeda(s) de {moeda_b}")
else:
    print("Impossível efetuar a troca")