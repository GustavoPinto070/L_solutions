def soma_mat(matriz1:list[list[int]], matriz2:list[list[int]])->list[list[int]]:
    """
    matriz1 = a = (m x n), 0 < i < m, 0 < j < n, cada elemento é dado por aij
    matriz2 = b = (m x n), 0 < i < m, 0 < j < n, cada elemento é dado por bij
    m = numero de linhas e "altura" da matriz
    n = numero de colunas e "largura" da matriz
    i = "altura" do elemento xij, com indice 0 no topo, crescendo para baixo
    j = "largura" do elemento xij, com indice 0 na esquerda, crescendo para a direita
    """
    matriz_resultante = []                                # m x n
    if len(matriz1) != len(matriz2):                        # m1 != m2
        raise ValueError("soma_mat: matrizes com numero de linhas diferente")
    for i in range(len(matriz1)):                           # por cada i in range(m)
        linha = []                                          # len(linha) = n
        if len(matriz1[i]) != len(matriz2[i]):              # n1 != n2
            raise ValueError("soma_mat: matrizes com numero de colunas diferente")
        for j in range(len(matriz1[i])):                    # por cada i in range(n)
            linha.append(matriz1[i][j] + matriz2[i][j])     # cada elemento da linha vai ser a soma entre aij e bij
        matriz_resultante.append(linha)                     # a matriz resultante é a lista de linhas (m x n)
    return matriz_resultante

def soma_mat_resumo(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[i]))] for i in range(len(m1))]

if __name__ == "__main__":
    from ex5 import escreve_matriz
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    escreve_matriz(r1:=soma_mat(m1, m2))
    escreve_matriz(r2:=soma_mat_resumo(m1, m2))
    print(f"Test -> {r1 == r2}")
