gols_a = int(input('gols A: '))
gols_b = int(input('gols B: '))

#time A venceu 
if gols_a > gols_b:
    print("Time A ganhou")

else:
    #time B venceu
    if gols_a < gols_b:
        print('Time B ganhou')
    #deu empate
    else:
        print('Deu empate!')