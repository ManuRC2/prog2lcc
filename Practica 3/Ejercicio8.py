from math import floor

def busqueda_dicotomica(lista, palabra):
    # print(lista)
    if len(lista) == 1:
        return lista[0] == palabra
    mitad = floor(len(lista)/2)
    if lista[mitad] > palabra:
        return busqueda_dicotomica(lista[:mitad], palabra)
    return busqueda_dicotomica(lista[mitad:], palabra)


lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(busqueda_dicotomica(lista, "f"))