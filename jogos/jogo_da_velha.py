tabuleiro = []
i = 0
while i < 3:
    tabuleiro.append([''] * 3) 
    i = i + 1
    
tabuleiro[0][2] = 'x';
tabuleiro[1][0] = 'o';
tabuleiro[1][1] = 'x';
tabuleiro[2][0] = 'o';
for i in tabuleiro:
    print(i)
# for i in tabuleiro(3):
#     tabuleiro.append(['', '', '']) 
    
