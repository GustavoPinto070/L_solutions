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
nsi = |999 - ns| = |999 - 99i| = 99(11 - i) (|999 - ns| caso ns tenha 3 dígitos, o que é verdade pois i>=2*)
Portanto, ns + nsi = 99i + 99(11 - i) = 99 * 11 = 1089.
Portanto, a função retorna sempre 1089.

*(Se ns tivesse 2 dígitos ou um dígito, respetivamente seria, nsi = |99 - ns| e nsi = |9 - ns|, que altera o resultado final)
(ns tem dois dígitos se i=1 e um dígito se i=0, daí a condição i>=2)
"""

# Juro que cheguei a estas conclusões sem chatgpt :D (ja tinha feito isto antes)

