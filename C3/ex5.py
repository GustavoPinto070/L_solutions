def triangular(n):
    if n <= 0:
        return False
    m = 0
    t = 0
    while t < n:
        m += 1
        t += m
    if t == n:
        return True
    return False

# Test the function
if __name__ == "__main__":
    print("Introduza um número inteiro positivo\n(-1 para terminar)")
    while True:
        num = int(input("Número: "))
        if num == -1:
            break
        print(f"O número {num} é triangular? {triangular(num)}")