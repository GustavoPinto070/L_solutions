def conta_linhas(nome_f: str):
    with open(nome_f, 'r',) as f:
        return sum(1 for l in f if l.strip())

if __name__ == "__main__":
    print(conta_linhas('f1_teste.txt')) # For this to work properly, the script has to be run inside L10 (cd L10)