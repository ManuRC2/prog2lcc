from math import trunc

# (horas, minutos)
# Ej: 16:45 = (16, 45)
# Max horas = 24
# Max minutos = 60

def arreglarTiempo(tiempo: tuple[int, int]):
    return ((tiempo[0]%24)+trunc(tiempo[1]/60), tiempo[1]%60)

def sumaTiempo(t1: tuple[int, int], t2: tuple[int, int]):
    return arreglarTiempo((t1[0]+t2[0], t1[1]+t2[1]))

if __name__ == "__main__":
    print(sumaTiempo((16, 45), (8, 60)))