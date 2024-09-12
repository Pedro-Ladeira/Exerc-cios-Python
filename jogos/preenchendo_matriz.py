# Usando while
num = 1
linha = 0
matriz = []
while linha < 4:
    pos = 0
    while pos < 5:
        matriz[linha][pos] = num
        num = num + 1
        
for i in matriz:
    print(i)
    


# Usando for
# matriz = []
# for i in range (4):
#     matriz.append([0] * 5)

# num = 1
# for i in range(4):
#     for j in range(5):
#         matriz[i][j] = num
#         num = num + 1
# for linha in matriz:
#     print(linha)