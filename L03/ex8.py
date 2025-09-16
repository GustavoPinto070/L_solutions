while True:
    print("Escreva um número de segundos\n(um número negativo para terminar)")
    s = int(input("? "))
    if s < 0:
        break
    print(f"O número de dias correspondentes é {s/86400:.18f}")