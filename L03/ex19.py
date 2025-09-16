n = 123456789
i = 1
while i < 10:
    left = n // (10 ** (9 - i)) # left é n com os últimos (9 - i) dígitos removidos
    result = left * 8 + i        # result é left x 8 + i
    print(left, "x 8 +", i, "=", result)
    i += 1