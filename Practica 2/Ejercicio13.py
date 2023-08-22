def es_potencia_de_dos(n):
    if n == 2:
        return True
    if n % 2 != 0:
        return False
    return es_potencia_de_dos(n/2)

def potencias_de_dos(n, m):
    res = []
    for x in range(n, m+1):
        if es_potencia_de_dos(x):
            res.append(x)
    return res

if __name__ == '__main__':
    print(potencias_de_dos(3, 4545))