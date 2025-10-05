def resumo_FP(notas_dict: dict) -> tuple[float, int]:

    if notas_dict == {}: # Evitar divisão por zero se não houver alunos
        return (0, 0)
    
    total_reprovados = 0
    nota_aprovados = 0
    total_aprovados = 0

    for nota in notas_dict:
        if nota < 10:
            total_reprovados += len(notas_dict[nota])
        else:
            nota_aprovados += nota * len(notas_dict[nota])
            total_aprovados += len(notas_dict[nota])

    return (nota_aprovados / total_aprovados, total_reprovados)

print(resumo_FP({1 : [46592, 49212, 90300, 59312], 15 : [52592, 59212], 20 : [58323]}))
