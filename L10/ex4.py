def concatena(lista_nomes_fe: list[str], nome_fs: str):
    with open(nome_fs, 'w') as fs:
        for nome_fe in lista_nomes_fe:
            with open(nome_fe, 'r') as fe:
                for l in fe:
                    fs.write(l)

if __name__ == "__main__":
    concatena(["f1_teste.txt", "f2_teste.txt"], "concatena_res.txt")