def eliminaDuplicados(lista):
    return [q for i, q in enumerate(lista) if q not in lista[:i]]

if __name__ == "__main__":
    print(eliminaDuplicados([1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 8, 9, 19, 8, 6, 4, 23, 4]))