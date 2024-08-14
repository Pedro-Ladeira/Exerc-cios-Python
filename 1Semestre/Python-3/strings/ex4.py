frase = input("Digite uma frase: ")
letra = input("Digite os caracteres: ")

resp = ""
letra = letra.lower()
letraM = letra.upper()

for c in frase:
    if c in letra or c in letraM:
        resp = resp + "*"
    else:
        resp = resp + c

print(resp)