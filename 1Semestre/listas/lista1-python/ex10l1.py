distancia = float(input("informe a distancia percorrida em metros: "))
tempo = float(input("informe o tempo em segundos: "))

result = distancia / tempo

print(f"A velocidade em m/s é de {result}")

distanciakm = distancia /1000
tempohrs = tempo / 3600    
velocidadekmhr = distanciakm / tempohrs

print(f"a velocidade em km/horas é de {velocidadekmhr}")