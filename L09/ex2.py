def agrupa_por_chave(l: list[tuple[str, int]]):
    d = {}
    for k, v in l:
        if k not in d:
            d[k] = []
        d[k].append(v)
    return d
