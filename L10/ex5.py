def procura(palavra: str, nome_f: str):
    with open(nome_f, 'r') as f:
        for l in f:
            if l.find(palavra) != -1:
                print(l, end='')

if __name__ == "__main__":
    procura("my", "inverte_res.txt")