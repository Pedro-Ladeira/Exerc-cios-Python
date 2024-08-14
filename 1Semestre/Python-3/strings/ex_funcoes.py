import os 
def clean():
    os.system("cls")

print("1.aumento  \n2.divisão")
escolha = int(input("Escolha uma opção: "))

if escolha == 1:
    clean()
    valor = float(input("informe o valor: "))
    percentual = float(input("informe o percentual de aumento: "))

    def aumento():
        novo_valor = (1 + percentual/100) * valor
        # print(novo_valor) NÃO RECOMENDO USAR O PRINT COMO RESULTADO DA FUNÇÃO 
        return novo_valor

    aux = aumento()
    # posso escolher o que fazer com o aux: gravar em um arquivo, gravar no banco de dados,
    # mandar para outro servidor, exibir na tela do meu celular ou navegador web
    print(aux)

elif escolha == 2:
    clean()
    a = float(input("iforme o dividendo: " ))
    b = float(input("Informe o divisor: "))
    def divisao(a, b):
        return a // b, a % b
    res = divisao(a, b)
    print(res)

else: 
    print("Informação errada!")
