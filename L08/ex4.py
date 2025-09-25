def elemento_matriz(matriz:list[list[int]], linha:int, coluna:int)->int:
    if coluna >= len(matriz):
        raise ValueError("elemento_matriz: indice invalido, coluna", coluna)
    elif linha >= len(matriz[coluna]):
        raise ValueError("elemento_matriz: indice invalido, linha", linha)
    return matriz[linha][coluna]

if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]

    try:
        print(elemento_matriz(m, 0, 0)) # 1
    except ValueError as e:
        print(e)