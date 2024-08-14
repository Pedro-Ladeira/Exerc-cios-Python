import baralho as bar

# jogo de truco: uma partida é uma melhor de 3
def pontos(carta):
    if carta[0] <= 3 and carta[0] >= 1:
        return carta[0] * 30
    elif carta[0] == 11:
        return 12
    elif carta[0] == 12: 
        return 11
    return carta[0]

def rodada(carta_h, carta_c):
    # -1 se humano ganhou a rodada
    # 0 se deu empate 
    # 1 se a CPU ganhou a rodada
    if pontos(carta_h) > pontos(carta_c):
        return -1
    elif pontos(carta_h) < pontos(carta_c):
        return 1
    else:
        return 0
    
def jogada(mao):
    print(bar.to_str_mao(mao))
    opcao = int(input("Digite a carta que deseja descartar (0, 1, 2, 3..): "))
    return mao.pop(opcao)

def jogada_cpu(mao):
    return mao.pop()

deck = bar.cria('truco')

bar.embaralha(deck)
mao_hum = bar.distribui(deck, 3)
mao_cpu = bar.distribui(deck, 3)
c_hum = jogada(mao_hum)
c_cpu = jogada_cpu(mao_cpu)
res = rodada(c_hum, c_cpu)
print(bar.to_str(c_hum), "X", bar.to_str(c_cpu))
if res == -1:
    print("Humano ganhou a primeira")
elif res == 1:
    print("CPU ganhou a primeira")
else:
    print("Empatou")
    
c_hum = jogada(mao_hum)
c_cpu = jogada_cpu(mao_cpu)
res2 = rodada(c_hum, c_cpu)
print(bar.to_str(c_hum), "X", bar.to_str(c_cpu))
if res2 == -1:
    print("Humano ganhou a primeira")
elif res2 == 1:
    print("CPU ganhou a primeira")
else:
    print("Empatou")
    