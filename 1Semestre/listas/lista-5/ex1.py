num1 = int(input("Informe um numero: "))
num2 = int(input("Informe outro numero: "))

if num1 > 0 or num2 > 0:
    media_geometrica = (num1 * num2) ** 0.5
    print(f"A média geometrica de {num1} e {num2} é {media_geometrica}")

else: 
    print("Digite um número real!")