n = int(input("Informe n: "))
 
# if n % 1 == 0 and n % n == 0:
#     print(f"{n} é primo")
# else: 
#     print(f"{n} não é primo")

divisor = 1
contador = 0

while divisor <= n:
    if n % divisor == 0:
        contador = contador + 1
    divisor = divisor + 1   

if contador == 2:
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")