def escreve_esparsa(d: dict[tuple[int, int], int]):
    max_linha = max(k[0] for k in d.keys())
    max_coluna = max(k[1] for k in d.keys())
    
    return "\n".join(
        " ".join(str(d.get((linha, coluna), 0)) for coluna in range(max_coluna + 1))
        for linha in range(max_linha + 1)
    )

print(escreve_esparsa({(2, 3): 5, (0, 1): 6, (2, 4): 2}))
