def multiplica_mat(matriz1:list[list[int]], matriz2:list[list[int]])->list[list[int]]:
    """
    matriz1 = a = (m x n), cada elemento é dado por aij
    matriz2 = b = (n x r), cada elemento é dado por bij
    """
    matriz_resultante = []
    for m in range(len(matriz1)):                       # por cada linha da primeira matriz
        linha = []
        for r in range(len(matriz2[0])):                # por cada coluna da segunda matriz
            if len(matriz1[0]) != len(matriz2):
                raise ValueError("multiplica_mat: as matrizes não são m x n e n x r, respetivamente") # n1 != n2
            soma = 0                                    # cada elemento da matriz_resultante vai ser a soma da multiplicação
            for n in range(len(matriz2)):               # por cada coluna da primeira matriz
          # for n in range(len(matriz1[0]))             # por cada linha da segunda matriz (same bs)
                soma += matriz1[m][n] * matriz2[n][r]   # a parte da multiplicação entre elementos da linha m e coluna r, somados
            linha.append(soma)                          # cada elemento é a soma das diferentes multiplicações (len(linha) = r)
        matriz_resultante.append(linha)                 # a matriz resultante é a lista de linhas (m x r)
    return matriz_resultante

def multiplica_mat_resumo(m1, m2):
    return [[sum(m1[m][n] * m2[n][r] for n in range(len(m2))) for r in range(len(m2[0]))] for m in range(len(m1))]

if __name__ == "__main__":
    from ex5 import escreve_matriz
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    escreve_matriz(r1:=multiplica_mat(m1, m2))
    escreve_matriz(r2:=multiplica_mat_resumo(m1, m2))
    print(F"Test -> {r1 == r2}")

    """
    30   36   42
    66   81   96
    102  126  150
    """