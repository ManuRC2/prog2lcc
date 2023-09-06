def safe_number_input(text = "Ingrese un número: "):
    flag = True
    while flag:
        try:
            x = int(input(text))
            flag = False
        except:
            print("Por favor, ingrese un número natural.")
    return(x)

def parse_casilla(casilla):
    match casilla:
        case 0:
            return " "
        case 1:
            return "o"
        case 2:
            return "x"

def mostrar_tablero(tab):
    for fila in tab:
        for cas in fila:
            print(f"|{parse_casilla(cas)}", end="")
        print("|")

def poner_ficha(tab, jug):
    numero_bien = False
    while not numero_bien:
        fil = safe_number_input(f"Jugador {jugador}, ingrese una fila: ") - 1
        col = safe_number_input(f"Jugador {jugador}, ingrese una columna: ") - 1
        if fil not in range(3) or col not in range(3):
            print("Ingrese un número dentro de la casilla")
        elif tab[fil][col] != 0:
            print("Esa casilla ya fue elegida!")
        else:
            numero_bien = True

    if tab[fil][col] == 0:
        tab[fil][col] = jug
    return tab

def alguien_gano(tab):
    estado = 3
    if tab[0][0] == tab[1][1] == tab[2][2]:
        estado = tab[0][0]
    if tab[2][0] == tab[1][1] == tab[0][2]:
        estado = tab[2][0]
    for fil in tab:
        if fil[0] == fil[1] == fil[2]:
            estado = fil[0]
    for i in range(3):
        if tab[0][i] == tab[1][i] == tab[2][i]:
            estado = tab[0][i]
    for fila in tab:
        for cas in fila:
            if cas == 0:
                estado = cas
    return estado

tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

victoria = 0
jugador = 1

while victoria == 0:
    tablero = poner_ficha(tablero, jugador)
    mostrar_tablero(tablero)
    victoria = alguien_gano(tablero)
    jugador = 1 if jugador == 2 else 2

match victoria:
    case 1:
        print("Gana el jugador 1!")
    case 2:
        print("Gana el jugador 2!")
    case True:
        print("Empate!")