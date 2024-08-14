import baralho

def soma_pontos(mao):
    ac = 0
    for carta in mao:
        if carta[0] > 10:
            ac = ac + 10
        else: 
            ac = ac + carta[0]
    return ac

def imprime(mao):
    print("Cartas")
    print(baralho.to_str_mao(monte))
    
monte = baralho.cria('normal')
baralho.embaralha(monte)

mao_humano = baralho.distribui(monte, 2)
mao_cpu = baralho.distribui(monte, 2)

print("Cartas")
print(baralho.to_str_mao(mao_humano))
pontos_humano = soma_pontos(mao_humano)
print(f"Pontos: {pontos_humano}")
resp = input("Você quer mais uma carta (s/n)?: ")

while resp == 's':
    carta = baralho.compra(monte)
    mao_humano.append(carta)
    imprime(mao_humano)
    resp = input("Você quer mais uma carta (s/n)?: ")

while soma_pontos(mao_cpu) < 16:
    carta = baralho.compra(monte)
    mao_cpu.append(carta)
    
print("Você")
imprime(mao_humano)
print("CPU")
imprime(mao_cpu)