def conta_vogais(nome_f):
    vogais = "aeiou"
    cont = {v: 0 for v in vogais}
    with open(nome_f, "r") as f:
        for l in f:
            for c in l.lower():
                if c in cont:
                    cont[c] += 1
    return cont

if __name__ == "__main__":
    print(conta_vogais('f1_teste.txt'))