def num_cpf(cpf):
    cpf_formatado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
    return cpf_formatado

cpf = input("Digite o CPF: ")

cpf_formatado = num_cpf(cpf)
print("CPF formatado:", cpf_formatado)