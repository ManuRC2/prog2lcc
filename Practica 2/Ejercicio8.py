from Ejercicio7 import positive_number_input

def promedio_notas(cant):
    notas = []
    for n in range(cant):
        notas.append(positive_number_input(f"Ingrese nota n° {n+1}: "))
    return(sum(notas)/cant)
    
if __name__ == '__main__':
    n = positive_number_input("¿Cuantas notas va a ingresar? ")
    print(f"Promedio: {promedio_notas(n)}")
