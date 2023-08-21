def duplica(s, n):
    return ((s + duplica(s, n-1)) if n > 0 else '')

if __name__ == '__main__':
    print(duplica("Hola!\n", 4))