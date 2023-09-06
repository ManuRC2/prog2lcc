def palabrasMayores(s, n=5):
    # 😳
    return len([q for q in s.split(' ') if len(q) > n])

if __name__ == "__main__":
    print(palabrasMayores("Hola todo correcto la verdad"))