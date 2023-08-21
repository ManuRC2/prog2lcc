def n_pares(n):
    if n <= 0:
        return
    print(n*2)
    n_pares(n-1)

n_pares(3)