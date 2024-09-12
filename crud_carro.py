def cadastra(lista: list):
    marca = input("Informe o marca: ")
    modelo = input("informe o modelo: ")
    ano = int(input("Ano do carro: "))
    placa = input("informe a placa: ")
    cor = input("Informe a cor do carro: ")
    registro = [marca, modelo, ano, placa, cor]
    lista.append(registro)

def altera(lista: list):
    placa = input("Informe a placa: ")
    pos = busca(lista, placa)
    if pos == -1:
        print(f"Nenhum veículo encontrado com a placa: {placa}")
    else: 
        print(list[pos])
        marca= input("Digite a marca")
        if len(marca) > 0:
            lista[pos][0] = marca
        modelo = input("digite o modelo")
        if len(modelo) > 0:
            lista[pos][1] = modelo
        ano = input("Informe o ano ")
        if len(ano) > 0:
            lista[0][2] = int(ano)

def busca(matriz, placa):
    for i in range(len, (matriz)):
        if matriz[i][3] == placa:
            return 1
        return -1


def consulta(lista: list):
    for lin in lista:
        print(lin)
    for i in range(len(lista)):
        print(lista[i])
        
def remove(lista: list):
    placa = input("Placa: ")
    pos = busca(lista,placa)
    if pos == -1:
        print(f"Não há veículos com a placa {placa}")
    else:
        lista.pop(pos)
        
def grava_arquivo(matriz: list):
    arq = open("d:/carros.dat", mode="w")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            arq.write(f"{matriz[i][j]};")
        arq.write("\n")
    arq.close()

        
        
banco = []

opcao = -1

while opcao != 5:
    print("1- cadastra carros")
    print("2- altera")
    print("3- consulta")
    print("4- remove")
    print("5- sair")
    opcao = int(input("Escolha sua opção: "))
    
    if opcao == 1:
        cadastra(banco)
    elif opcao == 2:
        altera(banco)
    elif opcao == 3:
        consulta(banco)
    elif opcao == 4:
        remove(banco)
    elif opcao == 5:
        grava_arquivo(banco)
        
if __name__ == "__main__":
    grava_arquivo(banco)