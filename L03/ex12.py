x = float(input("Qual o valor de x\n? "))
n = int(input("Qual o valor de n\n? "))
soma = anterior = i = 1
while i <= n:
    anterior *= x / i
    soma += anterior
    i += 1
print(f"O valor de e^{x} aproximado por {n} termos é {round(soma, 3)}")

# Same as
x = float(input("Qual o valor de x\n? "))
n = int(input("Qual o valor de n\n? "))
soma = 1
anterior = 1
atual = 1
i = 1
while i <= n:
    atual = anterior * x / i
    soma += atual
    anterior = atual
    i += 1
print("O valor de e^", x, "aproximado por", n, "termos é", round(soma, 3))