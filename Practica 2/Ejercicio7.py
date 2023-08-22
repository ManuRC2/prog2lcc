def positive_number_input(text = "Ingrese un número positivo: "):
    while True:
        try:
            x = int(input(text))
            if x > 0:
                return(x)
            else:
                print("El numero ingresado es negativo.")
        except:
            print("Por favor, ingrese un número natural positivo.")

if __name__ == '__main__':
    print(positive_number_input())