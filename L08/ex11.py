def transposta(matrizes: list):
    # Lista dos primeiros elementos de cada matriz pelo tamanho da linha (coluna por linha, linha por coluna)
    return [[matriz[i] for matriz in matrizes] for i in range(len(matrizes[0]))]

if __name__ == "__main__":
    print(transposta([[1, 2, 3], [4, 5, 6]]))