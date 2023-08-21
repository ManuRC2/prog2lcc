def sumatoria(n):
    if n <= 0:
        return 0
    return n + sumatoria(n-1)

if __name__ == '__main__':
    print(sumatoria(10))