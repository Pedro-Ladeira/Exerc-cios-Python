num = int(input("Digite um número: "))
resp = ""

while num != 0:
    resto = num % 16
    num = num // 16
    if resto == 10:
        resp = "A" + resp
    elif resto == 11:
        resp = "B" + resp
    elif resto == 12:
        resp = "c" + resp
    elif resto == 13:
        resp = "d" + resp
    elif resto == 14:
        resp = "e" + resp
    elif resto == 15:
        resp = "f" + resp
    else:
        ()

resp = str(resto) + resp
print(resp)