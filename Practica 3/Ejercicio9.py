def printInverso(s):
    flag = True
    i = -1
    while flag:
        if i + len(s) == 0:
            flag = False
        print(s[i])
        i-=1
    return

if __name__ == "__main__":
    printInverso("hola")