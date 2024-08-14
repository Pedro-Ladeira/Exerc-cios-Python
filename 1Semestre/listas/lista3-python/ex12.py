num = int(input("Digite o numero: "))

num_bak = num
soma = 0

while num != 0:
    dig = num % 10
    soma = soma * 10 + dig
    num = num // 10

#print(soma)
if num_bak == soma:
    print("é palindrome")
else:
    print("não é palindrome")