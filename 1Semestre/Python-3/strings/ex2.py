palavra = input("Digite a frase: ")
t = ""

i = 0

while i < len(palavra):
    t = t + palavra[i] + " "
    i = i + 1

print(t)