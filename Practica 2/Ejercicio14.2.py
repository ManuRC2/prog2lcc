from random import randint

def juego(n):
    ars = 0
    usd = 0
    for i in range(n):
        dado = randint(1, 6)
        match dado:
            case 1:
                print("1: No pasa nada")
            case 3:
                print("3: +1 USD")
                usd += 1
            case 6:
                print("6: +4 ARS")
                ars += 4
            case _:
                print(f"{dado}: -2 ARS")
                ars -= 2
    print(f"{n} dados tirados. Resultados:\nARS: {ars}\nUSD: {usd}")

if __name__ == "__main__":
    juego(100)