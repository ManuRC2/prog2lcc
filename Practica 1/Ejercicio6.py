def sum_range(n, m):
    if n+1 >= m:
        return 0
    return n+1 + sum_range(n+1, m)


if __name__ == '__main__':
    print(sum_range(2, 10))