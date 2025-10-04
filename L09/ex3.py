# Constantes
NAIPES = ('esp', 'copas', 'our', 'paus')
VALORES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')

# a)
def baralho():
    return [{'np': naipe, 'vlr': valor} for naipe in NAIPES for valor in VALORES]

# b)
def baralha(b):
    from random import random

    for i in range(len(b)):
        j = int(random()*(len(b)))
        b[i], b[j] = b[j], b[i]
    
    return b

# c)
def distribui(b, n):
    if len(b) % n != 0:
        raise ValueError("distribui: argumento inválido")
    
    cartas_por_jogador = b//n
    l = []
    for _ in range(n):
        l.append(b[-cartas_por_jogador:])
        b = b[:-cartas_por_jogador]
    
    return l