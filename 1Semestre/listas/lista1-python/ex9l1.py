precoproduto = float(input("informe o preço do produto:")) 
valordesconto = float(input("informe o porcentual do desconto: "))
desconto = precoproduto * valordesconto / 100

novovalor = precoproduto - desconto
aumento = desconto + precoproduto

print(f"o valor do produto com o desconto aplicado é {novovalor}")
print(f"E caso houvesse uum aumento seria para {aumento}")