def soma_mat(matriz1:list[list[int]], matriz2:list[list[int]])->list[list[int]]:
    matriz_resultante = [[]]
    if len(matriz1) != len(matriz2):
        raise ValueError("soma_mat: matrizes com numero de linhas diferente")
    for i in range(len(matriz1)):
        linha = []
        if len(matriz1[i]) != len(matriz2[i]):
            raise ValueError("soma_mat: matrizes com numero de colunas diferente")
        for j in range(len(matriz1[i])):
            linha.append(matriz1[i][j] + matriz2[i][j])
        matriz_resultante.append(linha)
    return matriz_resultante

if __name__ == "__main__":
    from ex5 import escreve_matriz
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    escreve_matriz(soma_mat(m1, m2))
