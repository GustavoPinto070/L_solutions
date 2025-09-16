print(sum(map(int, input("Introduza um número inteiro positivo: "))))

# Without using map and sum
n = int(input("Introduza um número inteiro positivo: "))
soma = 0
while n > 0:
    digito = n % 10
    soma += digito
    n //= 10
print(soma)