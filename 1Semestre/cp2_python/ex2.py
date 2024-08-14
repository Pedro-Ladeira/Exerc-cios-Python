n = int(input("Digite a quantidade de produtos que deseja aumentar: "))

maior_percentual = 0
maior_reais = 0

for c in range(n):
    preco_atual = float(input(f"Digite o preço atual do {c+1}º produto: "))
    preco_reajustado = float(input(f"Digite o preço reajustado do {c+1}º produto: "))
    
    aumento_percentual = ((preco_reajustado - preco_atual) / preco_atual) * 100
    aumento_reais = preco_reajustado - preco_atual
    
    if aumento_percentual > maior_percentual:
        maior_percentual = aumento_percentual
    if aumento_reais > maior_reais:
        maior_reais = aumento_reais

print(f"Maior aumento percentual: {maior_percentual}%")
print(f"Maior aumento em reais: {maior_reais}R$")
