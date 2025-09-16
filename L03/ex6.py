print(f"O maior dos {(n:=3)} números é {max([float(input(f'Introduza o {i+1}º número: ')) for i in range(n)]):.2f}")

# Without arrays or for-loops or the max() function
soma = 0
n1 = float(input("Introduza o 1º número: "))
n2 = float(input("Introduza o 2º número: "))
n3 = float(input("Introduza o 3º número: "))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f"O maior dos 3 números é {maior:.2f}")
