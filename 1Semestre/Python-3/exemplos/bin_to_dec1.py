#Transforme os seguintes n´umeros de bin´ario para decimal:
# 101011, 10110 e 10001

num_1 = 101011
num_2 = 10110
num_3 = 10001
soma = 0
soma2 = 0
soma3 = 0

potencia = 1
potencia2 = 1
potencia3 = 1

while num_1 > 0:
    dig = num_1 % 10
    num_1 = num_1 // 10
    soma = soma + dig * potencia
    potencia = potencia * 2
while num_2 > 0:
    dig2 = num_2 % 10
    num_2 = num_2 // 10
    soma2 = soma2 + dig2 * potencia2
    potencia2 = potencia2 * 2
while num_3 > 0:
    dig3 = num_3 % 10
    num_3 = num_3 // 10
    soma3 = soma3 + dig3 * potencia3
    potencia3 = potencia3 * 2

print(soma, soma2, soma3)