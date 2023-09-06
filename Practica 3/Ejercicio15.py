from math import trunc

# (Dia, Mes, Año): tuple[int, int, int]

def arreglarFechaE(fecha: tuple[int, int, int]):
    match fecha[1]:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            dias = 31
        case 2:
            # si es año bisiesto son 29
            dias = 29 if (fecha[2]%4)==0 else 28
        case _:
            dias = 30

    dia_f = fecha[0]
    dias2mes = 0
    if dia_f>dias:
        dias2mes = trunc(dia_f/dias)
        dia_f = dia_f%dias

    mes_f = fecha[1]+dias2mes
    meses2año = 0
    if mes_f > 12:
        meses2año = trunc(mes_f/12)
        mes_f = mes_f%12

    año_f = fecha[2]+meses2año

    return (dia_f, mes_f, año_f)

def diaSiguienteE(fecha: tuple[int, int, int]):
    return arreglarFechaE((fecha[0]+1, fecha[1], fecha[2]))

if __name__ == "__main__":
    print(diaSiguienteE((31, 12, 2003)))