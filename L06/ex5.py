from ex2 import explode
from ex3 import implode_for
from ex4 import filtra_pares

def algarismos_pares(n:int) -> int:
    return implode_for(filtra_pares(explode(n)))

"""
def algarismos_pares(n: int) -> int:
    # explode(n)
    if type(n) != int or n <= 0:
        raise ValueError("explode: argumento não inteiro positivo")
    digits = ()
    temp = n
    while temp > 0:
        ultimo_digito = temp % 10
        temp //= 10
        digits += (ultimo_digito, )
    digits = digits[::-1]

    # filtra_pares
    pares = ()
    for elem in digits:
        if not isinstance(elem, int) or elem < 0 or elem > 9:
            raise ValueError("filtra_pares: elemento não algarismo")
        elif elem % 2 == 0:
            pares += (elem,)

    # implode_for
    resultado = 0
    for elem in pares:
        if not isinstance(elem, int) or elem < 0:
            raise ValueError("implode_for: elemento não algarismo")
        resultado = resultado * 10 + elem

    return resultado
"""

# Test the function
if __name__ == "__main__":
    print("Introduza um número inteiro\n(-1 to exit)")
    while True:
        n = int(input("? "))
        if n == -1:
            break
        print(algarismos_pares(n))