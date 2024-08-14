print("Locadora FIAP")
print("1 - Alugar carro\n2 - Cadastrar cliente")
print("3 - Consultar carro\n4 - Análise de crédito")
print("5 - Fale conosco\n6 - Sair")
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    cpf = int(input("Informe o seu CPF: "))
    categoria = input("Informe a categoria do carro (Básico, premium e luxo): ")
    print("cod: 239 BMW 320i 2020 R$500,00")
    print("cod: 254 Mercedes Benz GLA 2022 R$580,00")
    print("cod: 215 Audi Q5 2021 R$700,00")
    codigo = int(input("Informe o código do carro que deseja: "))
    dias = int(input("Informe a quantidade de dias: "))
    print(f"Você alugou uma Q5 e vai pagar {dias * 700}")

elif opcao == 2:
    pass
elif opcao == 3:
    pass
elif opcao == 4:
    pass
elif opcao == 5:
    email = input("Informe seu email: ")
    pergunta = input("Pergunta/dúvida: ")
    print(f"Em breve entraremos em contato ou responderemos sua pergunta pelo seu email {email}")
elif opcao == 6:
    print("Obrigado por ultilizar nosso sistema!") 
else: 
    print("Opção inválida!")