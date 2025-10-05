def conta_palavras(expr: str) -> dict[str, int]:
    d_res: dict[str, int] = {}

    lista_de_palavras = expr.split() # Split separa uma string e transforma em lista, recortando por default pelos espaços e/ou newlines

    for palavra in lista_de_palavras:
        d_res[palavra] = d_res.get(palavra, 0) + 1 # __dict__.get(key, default) vai tentar buscar o valor na key assinalada e retorna ou o valor ou o default se o valor ainda não existir

    return d_res
