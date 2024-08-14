n = int(input("Digite n: "))

acumulador = 0
num = 1

while num <= n:
    acumulador = acumulador + num
    num = num + 1

print(acumulador)