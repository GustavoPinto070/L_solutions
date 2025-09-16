m = int(input("Introduza um número inteiro positivo (m)\n?  "))
n = int(input("Introduza outro número inteiro positivo (n)\n?  "))
parte_inteira = 0
parte_decimal = 0
while m >= n:
    m -= n
    parte_inteira += 1
if m == 0:
    print("A divisão é exata (m é divisível por n):", parte_inteira)
else:
    while m != 0 and parte_decimal < 10**6:
        m *= 10
        digito = 0
        while m >= n:
            m -= n
            digito += 1
        parte_decimal = parte_decimal * 10 + digito
    print("A divisão não é exata (m não é divisível por n):", str(parte_inteira) + "." + str(parte_decimal))
