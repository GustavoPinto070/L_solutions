from math import sqrt

n = 5
nums = [float(input(f"Introduza o {i+1}º número: ")) for i in range(n)]
average = sum(nums)/n
print(f"A média dos números é {average:.2f}")
desvio_padrão = sqrt(sum((x-average)**2 for x in nums)/(n-1))
print(f"O desvio padrão é {desvio_padrão:.2f}")

# Without arrays or for-loops
soma = 0
n1 = float(input("Introduza o 1º número: "))
n2 = float(input("Introduza o 2º número: "))
n3 = float(input("Introduza o 3º número: "))
n4 = float(input("Introduza o 4º número: "))
n5 = float(input("Introduza o 5º número: "))
soma = n1 + n2 + n3 + n4 + n5
average = soma / 5
print(f"A média dos números é {average:.2f}")
desvio_padrão = sqrt(((n1-average)**2 + (n2-average)**2 + (n3-average)**2 + (n4-average)**2 + (n5-average)**2)/4)
print(f"O desvio padrão é {desvio_padrão:.2f}")