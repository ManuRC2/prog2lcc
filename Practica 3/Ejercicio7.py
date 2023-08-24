from Ejercicio6 import eliminaDuplicados

def myLen(lista):
    if not lista:
        return 0
    return 1 + myLen(lista[:-1])

def elemsDistintos(lista):
    return myLen(eliminaDuplicados(lista))

print(elemsDistintos([1,2,3,4,5,6,10,4,3,4,5,1]))