from random import random, randint, randrange

"""
Tira un d6 hasta que salga n
"""
def d6(n):
    i = 0
    while True:
        x = randint(1, 6)
        i += 1
        print(f"Tirada {i}: {x}")
        if x == n:
            return i
        
def dados_iguales(n):
    iguales = 0
    for x in range(n):
        if randint(1, 6) == randint(1, 6):
            iguales += 1
    print(f"{iguales} de {n} tiradas fueron iguales.")
    print(f"{iguales*100/n}% de las tiradas.")


if __name__ == '__main__':
    dados_iguales(10000)
