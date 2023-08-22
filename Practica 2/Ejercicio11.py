CONTRASEÑA = "hola1234"
INTENTOS = 3

def contraseña_correcta(x):
    return x == CONTRASEÑA

if __name__ == '__main__':
    i = 0
    while i < INTENTOS and i >= 0:
        intento = input(f"Ingrese la contraseña ({INTENTOS-i} intentos): ")
        i+=1
        if contraseña_correcta(intento):
            i = -1
    if i == -1:
        print("Contraseña correcta! Ingresando...")
    else:
        print("Ha hecho demasiados intentos incorrectos. Saliendo.")