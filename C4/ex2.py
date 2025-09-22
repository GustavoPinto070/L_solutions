def conta_menores(tuple, num):
    total = 0
    for valor in tuple:
        if valor < num:
            total += 1
    return total

# Test the function
print("Introduza uma tupla de números inteiros (separados por vírgulas)\n(-1 para terminar)")
while True:
    user_input = eval(input("Tupla: "))
    if user_input == "-1":
        break
    number = int(input("Número: "))
    if number == -1:
        break
    total = conta_menores(user_input, number)
    print(f"Número de elementos menores que {number}: {total}\n")
    print(f"Test -> {sum(1 for x in user_input if x < number) == total}\n")

# You can use the built-in sum function with a generator expression to verify the result