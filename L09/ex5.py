def metabolismo(d: dict[str, tuple[str, int, float, int]]) -> dict[str, float]:
    d_res: dict[str, float] = {}

    for pessoa in d:
        genero = d[pessoa][0]
        idade: int = d[pessoa][1]
        altura_cm = d[pessoa][2]
        peso = d[pessoa][3]

        if genero == "M":
            d_res[pessoa] = round(66 + 6.8 * idade + 12.9 * altura_cm + 6.3 * peso, 3)
        elif genero == "F":
            d_res[pessoa] = round(655 + 4.7 * idade + 4.7 * altura_cm + 4.3 * peso, 3)
    
    return d_res
