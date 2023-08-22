def n_triangulares(nums):
    for n in range(1, nums+1):
        print(f"{n} - {sum(range(1, n+1))}")

if __name__ == '__main__':
    n_triangulares(5)