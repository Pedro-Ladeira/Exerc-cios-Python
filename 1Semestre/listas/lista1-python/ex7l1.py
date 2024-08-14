numero = int(input("escolha um numero entre 0 e 99: "))
unidade = numero % 10
dezena = numero // 10

if numero < 10:
    print(f"unidade é {unidade}")


elif numero > 99:
    print("numero inválido")

else:
    print(f"dezena é igual a {dezena} e unidade é igual a {unidade}")

