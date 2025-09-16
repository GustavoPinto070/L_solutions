m = {50: "notas de 50€", 20: "notas de 20€", 10: "notas de 10€", 5: "notas de 5€", 2: "moedas de 2€", 1: "moedas de 1€", 0.5: "moedas de 50 cêntimos", 0.2: "moedas de 20 cêntimos", 0.1: "moedas de 10 cêntimos", 0.05: "moedas de 5 cêntimos", 0.02: "moedas de 2 cêntimos", 0.01: "moedas de 1 cêntimo"}
v = float(input("Introduza o valor (em €) a converter em notas e moedas\n? "))
for nota in m:
    if v >= nota:
        print(f"{int(v//nota)} {m[nota]}") # imprime número de notas/moedas e o tipo
        v %= nota                          # atualiza valor para o que falta converter

# Without using for-loops or arrays
v = float(input("Introduza o valor (em €) a converter em notas e moedas\n? "))
v = v * 100 # Converter para cêntimos
if v >= 5000:
    print(f"{int(v//5000)} notas de 50€")
    v = v % 5000
if v >= 2000:
    print(f"{int(v//2000)} notas de 20€")
    v = v % 2000
if v >= 1000:
    print(f"{int(v//1000)} notas de 10€")
    v = v % 1000
if v >= 500:
    print(f"{int(v//500)} notas de 5€")
    v = v % 500
if v >= 200:
    print(f"{int(v//200)} moedas de 2€")
    v = v % 200
if v >= 100:
    print(f"{int(v//100)} moedas de 1€")
    v = v % 100
if v >= 50:
    print(f"{int(v//50)} moedas de 50 cêntimos")
    v = v % 50
if v >= 20:
    print(f"{int(v//20)} moedas de 20 cêntimos")
    v = v % 20
if v >= 10:
    print(f"{int(v//10)} moedas de 10 cêntimos")
    v = v % 10
if v >= 5:
    print(f"{int(v//5)} moedas de 5 cêntimos")
    v = v % 5
if v >= 2:
    print(f"{int(v//2)} moedas de 2 cêntimos")
    v = v % 2
if v >= 1:
    print(f"{int(v//1)} moedas de 1 cêntimo")