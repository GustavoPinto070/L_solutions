def seq_racaman(n:int)->list[int]:
    resultado = [0]            # r(0) = 0
    for i in range(1, n):      # começa em 1 pois resultado[0] já está definido
        # condição da sequência de racaman traduzida para python:
        if (resultado[i-1] > i) and ((resultado[i-1] - i) not in resultado):
            resultado.append(resultado[i-1] - i)
        else:
            resultado.append(resultado[i-1] + i)
    return resultado

if __name__ == "__main__":
    print(seq_racaman(15)) # [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9]