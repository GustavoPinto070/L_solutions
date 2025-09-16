print(f"Resultado: {''.join([l for l in input('Escreva um inteiro? ')if int(l)&1==1])}")

# Without list comprehension and for-loops and string join() and string concatenation
n = int(input("Escreva um inteiro? "))
resultado = 0
mult = 1
while n > 0:
    digito = n % 10                 # retrieve último dígito
    n //= 10                        # remove último dígito
    if digito % 2 == 1:             # if igito ímpar
        resultado += digito * mult  # add dígito à resposta
        mult *= 10                  # update multiplicador
print("Resultado:", resultado)