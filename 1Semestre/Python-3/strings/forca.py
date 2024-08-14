palavra = "cadeira"
erros = 0
segredo = ""

for c in palavra:
    # segredo = f"{segredo}_"
    segredo = segredo + "_ "

print(f"{segredo}\nErros: {erros}")
letra = input("Digite uma letra: ")

segredo = ""
for c in palavra:
    if c in letra:
        segredo = segredo + c + " "
    else:
        segredo = segredo + "_ "

print(f"{segredo}\nErros: {erros}")

