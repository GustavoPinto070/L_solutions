def implode_for(t: tuple) -> int:
    resultado = 0
    for elem in t:
        if not isinstance(elem, int) or elem < 0:
            raise ValueError("implode_for: elemento não algarismo")
        resultado = resultado * 10 + elem
    return resultado

def implode_while(t: tuple) -> int:
    resultado = 0
    i = 0
    while i < len(t):
        elem = t[i]
        if not isinstance(elem, int) or elem < 0:
            raise ValueError("implode_while: elemento não algarismo")
        resultado = resultado * 10 + elem
        i += 1
    return resultado

# Test the functions
if __name__ == "__main__":
    print("Introduza um tuplo (x, y, z, ...) de números inteiros positivos\n(-1 to exit)")
    while True:
        n = eval(input("? "))
        if n == -1:
            break
        print("For:", implode_for(n))
        print("While:", implode_while(n))
        print("Test ->", implode_for(n) == implode_while(n))
