n = int(input("Escreva um número para eu escrever a tabuada da multiplicação\nNum -> "))
for i in range(1, 11): print(n, "x", i, "=", n * i)

# Without using for-loops
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1