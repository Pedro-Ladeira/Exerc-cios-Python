candidatos = 6

conta20 = 0 
conta21a50 = 0 
conta50 = 0


nota = int(input("Digite a pontuação do candidato:"))
contador = 1
maior_nota = nota
menor_nota = nota

if nota <= 20:
    conta20 = conta20 + 1
elif nota <= 50:
    conta21a50 = conta21a50 + 1
else:
    conta50 = conta50 + 1

while contador < candidatos:
    nota = int(input("digite a pontuação do candidato: "))
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota
    contador = contador + 1

    if nota <= 20:              
        conta20 = conta20 + 1
    elif nota <= 50:
        conta21a50 = conta21a50 + 1
    else:
        conta50 = conta50 + 1

print(f"a maior nota foi {maior_nota} ")