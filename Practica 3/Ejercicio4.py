def ordenada(lista):
    for (a,b) in zip(lista[:-1], lista[1:]):
        if a>b:
            return False
    return True

if __name__ == "__main__":
    print(ordenada([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(ordenada([1, 2, 3, 4, 5, 5, 4, 8, 9, 10]))