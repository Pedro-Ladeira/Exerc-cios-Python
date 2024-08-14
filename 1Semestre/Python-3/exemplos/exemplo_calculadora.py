num_a = float(input("Digite a: "))
op = input("Informe o operador (+=*/): ")
num_b = float(input("Digite b: "))

if op == '+':
    resultado = num_a + num_b

elif op == '-':
    resultado = num_a - num_b

elif op == '*':
    resultado = num_a * num_b

elif op == '/':
    resultado = num_a / num_b
print(f'O resultado vale {resultado}')