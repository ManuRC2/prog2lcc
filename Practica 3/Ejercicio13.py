from random import sample

palos = ("Diamantes", "Corazones", "Picas", "Tréboles")
valores = ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")
mazo = [(a, b) for a in palos for b in valores]

def poker(cartas):
    # print(cartas)
    for carta in cartas:
        p = 0
        for carta2 in cartas:
            if carta[1] == carta2[1]:
                p+=1
        if p >=4:
            print("Mano ganadora: ", cartas)
            return True
    return False


if __name__ == "__main__":
    # cartas_poker = (('Diamantes', 2), ('Corazones', 2), ('Picas', 5), ('Picas', 2), ('Tréboles', 2))
    # print(poker(cartas_poker))
    ganadora = False
    i = 0
    while not ganadora:
        i+=1
        numeros_rand = sample(range(len(mazo)), 5)
        cartas_rand = [mazo[i] for i in numeros_rand]
        ganadora = poker(cartas_rand)
    print(f"Intentos: {i}")