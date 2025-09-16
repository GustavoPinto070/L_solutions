n = int(input("Escreva um inteiro\n? "))
z = 0
while n > 1:
    if n % 10 == 0 and n % 100 == 0: # Ultimo dígito é 0 e penúltimo também
        z += 1                       # Incrementa contador
    n //= 10                         # Remove último dígito
print(f"O número tem {z} pares de zeros seguidos")