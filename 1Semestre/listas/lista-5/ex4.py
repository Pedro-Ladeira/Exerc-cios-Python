def eh_primo(n):
    if n == 1:
        return False
    else:
        divisor = 2
        while n % divisor != 0:
            divisor = divisor + 1

        if n == divisor:
            return True
        else:
            return False

num = 2
contador = 0
while contador < 100:
    resp = eh_primo(num)
    if resp:
        contador = contador + 1
        print(num)
    num = num + 1