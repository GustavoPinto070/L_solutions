def escreve_matriz(matriz:list[list[int]]):
    resultado = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            resultado += "{:<5}".format(matriz[i][j]) # f"{matriz[i][j]:<5}"
        resultado += "\n"
    print(resultado)

if __name__ == "__main__":
    escreve_matriz([[1, 2, 3], [4, 5, 6]])
