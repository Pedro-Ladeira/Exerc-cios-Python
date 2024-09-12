def cadastra(correio: dict):
    login = input("Informe o login: ")
    if not login in correio:
        msg = {"assunto": "Bem vindo ao 1TDSPV", "from": "admin", "msg": ""}
        correio[login] = []
    else:
        print("Já existe esse login!")

def envia(correio: dict):
    login = input("Informe o login: ")
    if login in correio:
        sub = input("Assunto: ")
        de = input("Remetente: ")
        msg = input("Mensagem: ")
        registro = {"assunto": sub, "from": de, "msg": msg}
        lista_msg = correio[login]
        lista_msg.append(registro)
    else: 
        print(f"{login} não encontrado!")

def le(correio: dict):
    login = input("Login: ")
    if login in correio:
            lista_msgs = correio[login]
            for msg in lista_msgs:
                print(msg)
    

escaninho = {}

opcao = 0
while opcao != 4:
    print("1 - Cadastro")
    print("2 - Enviar email")
    print("3 - Ler mensagem")
    print("4 - Sair")
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        cadastra(escaninho)
    elif opcao == 2:
        envia(escaninho)
    elif opcao == 3: 
        le(escaninho)