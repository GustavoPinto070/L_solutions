def inverte(nome_f1, nome_f2):
    f1 = open(nome_f1, 'r')
    f2 = open(nome_f2, 'w')
    ls = f1.readlines()
    for l in ls[::-1]:
        f2.write(l)
    f2.close()
    f1.close()

def better_inverte(nome_f1, nome_f2):
    with open(nome_f1, 'r') as f1, open(nome_f2, 'w') as f2:
        f2.writelines(reversed(f1.readlines()))

if __name__ == "__main__":
    inverte("f1_teste.txt", "inverte_res.txt")
    better_inverte("f1_teste.txt", "better_inverte_res.txt")