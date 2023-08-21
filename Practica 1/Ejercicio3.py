def n_pares_mayores_m(n, m):
    if n <= 0:
        return
    print((n * 2) + (m if m%2 == 0 else m-1))
    n_pares_mayores_m(n-1, m)


n_pares_mayores_m(20, 13)