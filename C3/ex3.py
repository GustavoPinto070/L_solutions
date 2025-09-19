def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
if __name__ == "__main__":
    print("Introduza um número inteiro positivo\n(-1 para terminar)")
    while True:
        num = int(input("Número: "))
        if num == -1:
            break
        print(f"O número {num} é primo? {primo(num)}")
