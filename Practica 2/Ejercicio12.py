def es_primo(n):
    for div in range(2,n):
        if n%div == 0:
            return False
    return True

def primos_menores(n):
    res = []
    for x in range(1, n+1):
        if es_primo(x):
            res.append(x)
    return res


if __name__ == '__main__':
    print(primos_menores(200))