# a)

def absoluto(x: int) -> int: # Eu sei que abs() existe, mas não foi introduzida
    if x < 0:
        return -x
    return x

def reverse(num: int) -> int:
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num //= 10
    return reverse

def misterio(num: int) -> int:
    if not 999 >= num >= 100:
        raise ValueError("Número deve ser um inteiro de 3 dígitos")
    elif absoluto(num % 10 - num // 100) <= 1:
        raise ValueError("A diferença entre o primeiro e o último dígito deve ser maior que 1")
    ni = reverse(num)
    ns = absoluto(num - ni)
    nsi = reverse(ns)
    return ns + nsi

# Test the function
if __name__ == "__main__":
    print("Digite um número de 3 dígitos para aplicar a função 'misterio'\n(-1 para sair)")
    while True:
        number = int(input("Número? "))
        if number == -1:
            break
        try:
            print(misterio(number))
        except ValueError as e:
            print(e)

# b) A função retorna sempre 1089.
"""
Seja um número de 3 dígitos abc tal que a diferença entre o primeiro e o último dígito seja maior que 1.
Seja i a diferença entre c e a, ou seja, i = |a - c| (i>=2).
ni = cba
ns = |abc - cba| = |100a + 10b + c - (100c + 10b + a)| = |99a - 99c| = 99|a - c| = 99i

99i = 100i - i = 100i - 100 + 100 - i = 100(i - 1) + 100 - i = 100(i - 1) + 90 + (10 - i) = 100(i - 1) + 10*9 + (10 - i);
ns: [(x, y, z) = (i - 1, 9, 10 - i)]*

nsi = (10 - i, 9, i - 1) = 100(10-i) + 90 + i - 1 = 1000 - 100i + 90 + i - 1 = 1089 - 99i
Portanto, ns + nsi = 99i + 1089 - 99i = 1089
Portanto, a função retorna sempre 1089.

*
((x, y, z) são respetivamente os dígitos das centenas, dezenas e unidades de ns)
(Caso i seja 1 ou 0, ns teria 2 dígitos ou um dígito, respetivamente)
(Nesses casos, o resultado final será diferente ou zero)
"""

# Juro que cheguei a estas conclusões sem chatgpt :D (ja tinha feito isto antes, parecido)
# Afinal precisei :P (não lembrava bem)


