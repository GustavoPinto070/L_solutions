def juntos(tuple: tuple) -> int:
    total = current = 1 
    last = tuple[0]
    for num in tuple[1:]:
        if last == num:
            current += 1
        else:
            last = num
            total = max(total, current)
            current = 1
    return max(total, current)

# Test the function
print("Introduza uma tupla de números inteiros (separados por vírgulas)\n(-1 para terminar)")
while True:
    user_input = eval(input("Tupla: "))
    if user_input == "-1":
        break
    max_consecutive = juntos(user_input)
    print(f"Número máximo de elementos iguais consecutivos: {max_consecutive}\n")
    
