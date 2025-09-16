n=input("Escreva um número\n-> ")
print(n + n[::-1])

# Without string concatenation (n[::-1] is string slicing and concatenation)
n = int(input("Escreva um número\n-> "))
left = n
right = 0
i = 0
while n > 0:
    digito = n % 10                  # retrieve último dígito
    n //= 10                         # remove último dígito
    right = right * 10 + digito      # append dígito à resposta
    i += 1                           # incrementa número de dígitos
print(left*(10**i) + right)          # i é o número de zeros correspondentes a dígitos de n a adicionar a left

# You can use the len() function to count the number of digits in a string (len(n) = i at the end of the loop)