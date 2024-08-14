cpf = int(input("Informe os 9 digitos do seu cpf: "))
soma = 0 

mult = 2

while cpf != 0:
    digito = cpf % 10
    cpf = cpf // 10
    soma = soma + digito * 2 
    mult = mult + 1 

resto = soma % 11
if resto < 2:
    print(0)
else:
    print(11 - resto)
