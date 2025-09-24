def filtra_pares(t: tuple) -> tuple:
    resultado = ()
    for elem in t:
        if not isinstance(elem, int) or n < 0 or n > 9:
            raise ValueError("filtra_pares: elemento não algarismo")
        elif elem % 2 == 0:
            resultado += (elem,)
    return resultado

# Test the function
if __name__ == "__main__":
    print("Introduza um tuplo de algarismos\n(-1 to exit)")
    while True:
        n = eval(input("? "))
        if n == -1:
            break
        print(filtra_pares(n))