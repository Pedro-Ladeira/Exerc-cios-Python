n = int(input("Informe a qtd de alunos: "))
soma = 0

notas = []

i = 0
while i < n:
    nota = float(input(f"Informe a nota do {i+1}° aluno: "))
    notas.append(nota)
    soma = soma + nota 
    i = i + 1

media = soma / n
print(f"A média da turma foi de {media}")
# print(notas)
acima = 0
abaixo = 0

for nota in notas:
    if nota < media:
        abaixo = abaixo + 1
    else:
        acima = acima + 1
        
print(f"A qtd de alunos abaixo da média é de {abaixo}")
print(f"A qtd de alunos acima da média é de {acima}")

