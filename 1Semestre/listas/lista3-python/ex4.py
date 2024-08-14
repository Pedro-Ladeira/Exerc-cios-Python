nota1 = float(input("Digite a primeira nota: "))

while nota1 < 0 or nota1 > 10:
    aux = input("Nota inválida, digite a primeira nota: ")
    nota1 = float(aux)
    
aux = input("Digite a segunda nota: ")
nota2 = float(aux)

while nota2 < 0 or nota2 > 10:
    aux = input("Nota inválida, digite a segunda nota: ")
    nota2 = float(aux)

media = (nota1 + nota2) / 2

print("A média vale {:.2f}" .format (media)) 