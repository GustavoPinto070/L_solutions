def posicoes_maximo(w:tuple)->tuple:
    posicoes_max = (0,)
    maximo = w[0]
    for i in range(1, len(w)):
        if w[i] == maximo:
            posicoes_max += (i,)
        elif w[i] > maximo:
            posicoes_max = (i,)
            maximo = w[i]
    return posicoes_max

# Test the function
if __name__ == "__main__":
    print("Introduza um tuplo de inteiros\n(-1 to exit)")
    while True:
        t = eval(input("? "))
        if t == -1:
            break
        print(posicoes_maximo(t))