num = int(input("Informe um numero: "))

resto = num % 2

#se o resto é igual a 0 entao imprime que é par

if resto == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")