def explode_cheats(n):
    if type(n) != int or n <= 0:
        raise ValueError("explode: argumento não inteiro positivo")
    resultado = ()
    for elem in str(n):
        resultado += ((int(elem)),)
    return resultado

# Without using string slicing

def explode(n):
    if type(n) != int or n <= 0:
        raise ValueError("explode: argumento não inteiro positivo")
    resultado = ()
    while n > 0:
        ultimo_digito = n % 10
        n //= 10
        resultado += (ultimo_digito, )
    return resultado[::-1]

# Test the function
if __name__ == "__main__":
    print("Enter a positive integer\n(-1 to exit)")
    while True:
        n = int(input("? "))
        if n == -1:
            break
        print(explode(n))
        print("Test ->", explode(n) == explode_cheats(n))