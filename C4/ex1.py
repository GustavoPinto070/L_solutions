def duplica(tuple: tuple) -> tuple:
    result = ()
    for num in tuple:
        result += (num, num)
    return result

# Test the function
print("Introduza uma tupla de números inteiros (separados por vírgulas)\n(-1 para terminar)")
while True:
    user_input = eval(input("Tupla: "))
    if user_input == "-1":
        break
    duplicated_tuple = duplica(user_input)
    print(f"Tupla duplicada: {duplicated_tuple}\n")
