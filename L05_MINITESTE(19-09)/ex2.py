# Escreva um programa que leia um inteiro positivo n e modifique todos os seus dígitos ímpares,
# somando-lhes 2 (o dígito 9 passa a ser 1). O programa deve imprimir o número modificado.

n = int(input("Escreva um inteiro positivo: "))
resultado = 0
i = 0
while n > 0:
    digito = n % 10 
    n = n // 10
    if digito % 2 == 1:
        digito = (digito+2) % 10
    resultado = resultado + digito * (10 ** i)
    i = i + 1
print("O número modificado é:", resultado)