print(f"O número invertido é {input('Escreva um número inteiro positivo? ')[::-1]}")

# You can use [::-1] to reverse a string
# Without converting to string and using string slicing and concatenation
n = int(input("Escreva um número inteiro positivo? "))
inverso = 0
while n > 0:
    digito = n % 10                  # retrieve último dígito
    n //= 10                         # remove último dígito
    inverso = inverso * 10 + digito  # append dígito à resposta
print("O número invertido é", inverso)