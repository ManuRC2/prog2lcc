OPERACIONES = ["Sumar", "Restar", "Multiplicar", "Dividir", "Elevar"]

def safe_number_input(text = "Ingrese un número: "):
    flag = True
    while flag:
        try:
            x = int(input(text))
            flag = False
        except:
            print("Por favor, ingrese un número natural.")
    return(x)


def sum(x, y):
    return x + y
def res(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y != 0:
        return x / y
    return "¡La división por 0 no está definida!"
def pot(x, y):
    return x ** y

def menu():
    for i, x in enumerate(OPERACIONES):
        print(f"{i+1}. {x}")
    print("0. Salir")

    q = safe_number_input("Elija una opción: ")
    if q > 0 and q <= 5:
        x = safe_number_input("Ingrese el primer número: ")
        y = safe_number_input("Ingrese el segundo número: ")
    match q:
        case 0:
            return
        case 1:
            print(f"{x} + {y} = \n{sum(x, y)}")
        case 2:
            print(f"{x} - {y} = \n{res(x, y)}")
        case 3:
            print(f"{x} * {y} = \n{mul(x, y)}")
        case 4:
            print(f"{x} / {y} = \n{div(x, y)}")
        case 5:
            print(f"{x} ^ {y} = \n{pot(x, y)}")
        case _:
            print("El numero ingresado no es válido.")
    menu()
        




if __name__ == '__main__':
    menu()
