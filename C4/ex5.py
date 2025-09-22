def junta_ordenados(tuple1: tuple, tuple2: tuple) -> tuple:
    tuple_junto = ()
    i, j = 0, 0
    while i < len(tuple1) and j < len(tuple2):
        if tuple1[i] < tuple2[j]:
            tuple_junto += (tuple1[i],)
            i += 1
        else:
            tuple_junto += (tuple2[j],)
            j += 1
    tuple_junto += tuple1[i:] + tuple2[j:]
    return tuple_junto

# Test the function
print("Introduza duas tuplas de números inteiros ordenados (separados por vírgulas)\n(-1 para terminar)")
while True:
    user_input1 = eval(input("Tupla 1: "))
    if user_input1 == "-1":
        break
    user_input2 = eval(input("Tupla 2: "))
    if user_input2 == "-1":
        break
    tuple_junto = junta_ordenados(user_input1, user_input2)
    print(f"Tupla junto: {tuple_junto}\n")
    print(f"Test -> {tuple(sorted(user_input1 + user_input2)) == tuple_junto}\n")

# You can use the built-in sorted function to verify the result
