def junta_ordenados(t1:tuple, t2:tuple)->tuple:
    resultado = ()
    i, j = 0, 0
    while i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            resultado += (t1[i],)
            i += 1
        else:
            resultado += (t2[j],)
            j += 1
    resultado += t1[i:] + t2[j:]
    return resultado

# Test the function
if __name__ == "__main__":
    print("Introduza dois tuplos de números inteiros\n(-1 to exit)")
    while True:
        t1 = eval(input("1? "))
        if t1 == -1:
            break
        t2 = eval(input("2? "))
        if t2 == -1:
            break
        print(junta_ordenados(t1, t2))
        print("Test ->", junta_ordenados(t1, t2) == tuple(sorted(t1 + t2)))

# Use sorted() to test the function