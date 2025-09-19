# Escreva um programa que leia um inteiro positivo n e calcule o produto dos seus divisores ímpares.

n = int(input("Escreva um inteiro positivo: "))
resultado = 1
i = 2
while i <= n//2:                        # Testar todos os inteiros entre 2 e n/2 (inclusive)
    if n % i == 0 and i % 2 == 1:       # i é divisor de n e é ímpar
        resultado = resultado * i
    i = i + 1                           # Pretty sure i forgot to increment i in the original code

print("O produto dos divisores ímpares é:", resultado)
