from ex3 import primo

def n_esimo_primo(n):
    i = 1
    total = 0
    while total < n:
        i += 1
        if primo(i):
            total += 1
    return i

# Test the function
if __name__ == "__main__":
    print("Introduza um número inteiro positivo\n(-1 para terminar)")
    while True:
        num = int(input("Número: "))
        if num == -1:
            break
        resultado = n_esimo_primo(num)
        print(f"O {num}º número primo é: {resultado}")