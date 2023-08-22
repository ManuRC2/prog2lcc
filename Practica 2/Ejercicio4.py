def safe_number_input(text = "Ingrese un número: "):
    flag = True
    while flag:
        try:
            x = int(input(text))
            flag = False
        except:
            print("Por favor, ingrese un número natural.")
    return(x)

def factorial(n):
    return (n * factorial(n-1)) if n > 0 else 1

if __name__ == '__main__':
    m = safe_number_input("¿Cuantos numeros quiere ingresar?\n")
    for x in range(m):
        n = safe_number_input()
        print(f"{n}! = {factorial(n)}")
    print(f"{m} factoriales calculados. Saliendo.")