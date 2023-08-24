def duplicado(lista):
    for i, elem in enumerate(lista, 1):
        for elem2 in lista[i:]:
            if elem == elem2:
                return True
    return False

if __name__ == "__main__":
    print(duplicado([1,2,3,4,5,6,7,8,9,10]))
