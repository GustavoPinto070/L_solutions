def multiplica_mat(matriz1:list[list[int]], matriz2:list[list[int]])->list[list[int]]:
    matriz_resultante = []
    for m in range(len(matriz1)):
        linha = []
        for r in range(len(matriz2[0])):
            if len(matriz1[0]) != len(matriz2):
                raise ValueError("multiplica_mat: as matrizes não são m x n e n x r respetivamente")
            soma = 0
            for n in range(len(matriz2)):
                soma += matriz1[m][n] * matriz2[n][r]
            linha.append(soma)
        matriz_resultante.append(linha)
    return matriz_resultante

if __name__ == "__main__":
    from ex5 import escreve_matriz
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    escreve_matriz(multiplica_mat(m1, m2))
    """
    30 36 42
    66 81 96
    102 126 150
    """