def posicionesMultiplo(l, n):
    res = []
    for e in range(0, len(l)):
        if (e+1)%n == 0:
            res.append(l[e])
    return res

if __name__ == "__main__":
    print(posicionesMultiplo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 4))