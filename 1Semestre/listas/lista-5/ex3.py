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
resp = eh_primo(79)
print(resp)