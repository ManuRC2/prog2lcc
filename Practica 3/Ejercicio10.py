def contar(x, s):
    i = 0
    for c in s:
        if x == c:
            i += 1
    return i

if __name__ == "__main__":
    print(contar("o", "hola como estas"))