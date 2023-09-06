def dominoTuplas(t1, t2):
    for x in t2:
        if t1[0] == x or t1[1] == x:
            return True
    return False
        
def dominoString(s1):
    fichas = s1.strip("[]").split(" ")
    f1 = fichas[0].split("-")
    f2 = fichas[1].split("-")
    for x in f2:
        if f1[0] == x or f1[1] == x:
            return True
    return False



if __name__ == "__main__":
    print(dominoTuplas((3, 4), (5, 4)))
    print(dominoString("[2-3 6-2]"))