def contarVocales(s):
    dictV = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for c in s.lower():
        if c in dictV.keys():
            dictV[c] += 1
    print("Cantidad de vocales:")
    for v in dictV:
        print(f"{v}: {dictV[v]}")
    return dictV


if __name__ == "__main__":
    contarVocales("HOLA como andas? Espero que todo bien")