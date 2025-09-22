def soma_els_atomicos(x: tuple|int) -> int:
    if isinstance(x, int):
        return x
    total = 0
    for elemento in x:
        total += soma_els_atomicos(elemento)
    return total

# Test the function
print("Introduza uma tupla de números inteiros e/ou tuplas (separados por vírgulas)\n(-1 para terminar)")
while True:
    user_input = eval(input("Tupla: "))
    if user_input == "-1":
        break
    total_sum = soma_els_atomicos(user_input)
    print(f"Soma dos elementos atómicos: {total_sum}\n")
