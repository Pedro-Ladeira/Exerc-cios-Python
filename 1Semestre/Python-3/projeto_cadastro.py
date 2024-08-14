def adiciona(lista, nome, cpf, tel, nasc):
    lista.append(nome)
    lista.append(cpf)
    lista.append(tel)
    lista.append(nasc)

banco_dados = []
resp = "s"
while resp != "n":
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Tel: ")
    dt_nasc = input("Data de Nascimento: ")
    resp = input("Deseja cadastrar mais alguêm? (s/n): ")
    adiciona(banco_dados, nome, cpf, telefone, dt_nasc)
    print(banco_dados)
    
banco_dados = ['pedro', '54352', '(11) 91088', '02/02/2000', 'joao', '423', '(11) 04219', '25/09/1999', 'maria', '529', '(21) 4124124', '14/08/2001']
i = 0
while i < len(banco_dados):
    print(f"{i} - {banco_dados[i]}: {banco_dados[i + 3]}")
    i = i + 4
resp = int(input("Qual pessoa deseja alterar: "))

nome = input(f"Nome ({banco_dados[resp]}): ")
if len(nome) > 0:
    banco_dados[resp] = nome 
    
cpf = input(f"CPF ({banco_dados[resp + 1 ]}): ")
if len(cpf) > 0:
    banco_dados[resp + 1] = cpf
    
tel = input(f"Tel ({banco_dados[resp + 2]}): ")
if len(banco_dados) > 0:
    banco_dados[resp + 2] = tel
    
print(banco_dados)
