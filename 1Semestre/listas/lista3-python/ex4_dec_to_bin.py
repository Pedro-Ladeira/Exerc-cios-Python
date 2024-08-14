decimal = int(input("Informe o número: "))

resposta = ""

while decimal > 0:
    resto = decimal % 2
    resposta = str(resto) + resposta
    decimal = decimal // 2

print(f"Bínario {resposta}")
