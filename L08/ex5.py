def escreve_matriz(matriz:list[list[int]]):
    resultado = ""
    for i in range(len(matriz)):
        resultado += "\n"
        for j in range(len(matriz[i])):
            resultado += str(matriz[i][j]) + " "
    print(resultado)

if __name__ == "__main__":
    escreve_matriz([[1, 2, 3], [4, 5, 6]])
