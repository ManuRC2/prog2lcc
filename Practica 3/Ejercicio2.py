def sumaAcumulada(lista):
    return [sum(lista[:n]) for n in range(1, len(lista)+1)]

if __name__ == "__main__":
    print(sumaAcumulada([1, 2, 3, 4, 5, 6, 7]))