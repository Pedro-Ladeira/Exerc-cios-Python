dia = 29
mes = 2
ano = int(input("Informe o ano: "))

if ano % 400 == 0:
    print("Data válida!")
elif ano % 100 == 0:
    print("Data inválida")
elif ano % 4 == 0:
    print("Data válida!")
else:
    print("Data inválida")