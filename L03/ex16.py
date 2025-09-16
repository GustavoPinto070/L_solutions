t = p = 0
while True:
    r = int(input("Introduza a nota do aluno\n(-1 para terminar)\n? "))
    if r == -1:
        break
    if 10 <= r <= 20: # nota válida
        p += 1
        t += 1
    elif 0 <= r < 10: # nota válida
        t += 1
    else: # nota inválida
        print("Número inválido")
print(f"Notas positivas: {p}\n Percentagem de positivas: {p / t * 100 if t > 0 else 0:.2f}%")