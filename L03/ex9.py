r = ""
while True:
    s = int(input("Escreva dígito\n(-1 para terminar)\n? "))
    if s == -1:
        break
    r += str(s)
print(f"O número é: {r}")

# Without string concatenation
numero = 0
while True:
    s = int(input("Escreva dígito\n(-1 para terminar)\n? "))
    if s == -1:
        break
    numero = numero * 10 + s
print(f"O número é: {numero}")