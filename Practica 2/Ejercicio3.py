def fichas_n(n = 6):
    for x in range(0, n+1):
        for y in range(0, x+1):
            print(f"{x}|{y}")

if __name__ == '__main__':
    fichas_n(6)