def maior_elemento(tuple: tuple) -> int:
    max = tuple[0]
    for num in tuple[1:]:
        if num > max:
            max = num
    return max

# Test the function
print("Introduza uma tupla de números inteiros (separados por vírgulas)\n(-1 para terminar)")
while True:
    user_input = eval(input("Tupla: "))
    if user_input == "-1":
        break
    max_value = maior_elemento(user_input)
    print(f"Maior elemento: {max_value}\n")
    print(f"Test -> {max(user_input)==max_value}\n")

# You can use the built-in max function to verify the result