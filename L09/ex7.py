def mostra_ordenado(d: dict):
    lista = list(d.keys())  # convert keys to a real list

    changes_made = True
    while changes_made:
        changes_made = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:  # lexicographic comparison
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                changes_made = True

    print() # Newline
    for elem in lista:
        print(f"{elem} {d[elem]}")

if __name__ == "__main__":
    from ex6 import conta_palavras
    mostra_ordenado(conta_palavras('a aranha arranha a ra a ra arranha a aranha nem a aranha arranha a ra nem a ra arranha a aranha'))

