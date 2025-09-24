def remove_multiplos(nums:list[int], div:int)->list[int]:
    for i in range(len(nums)-1,-1,-1): # do último elemento ao primeiro
        if nums[i] % div == 0:
            nums.pop(i)                # a lista é diretamente modificada
    return nums

test_list = [2, 3, 5, 9, 12, 33, 34, 45]
test_div = 3
print(r1:=(remove_multiplos(test_list, test_div))) # [2, 5, 34]

# percorrer a lista na ordem inversa, de forma a, ao remover um elemento,
# não alteramos os índices de todos os elementos que ainda iremos analisar,
# apenas alteramos os índices dos elementos já percorridos

# Chatgpt:
# Se removes da frente para trás, os índices mudam e saltas elementos.
# Se removes de trás para a frente, só mudam os já vistos → nada se perde.

# another way would be
def remove_multiplos_v2(nums:list[int], div:int)->list[int]:
    i = 0
    while i < len(nums):
        if nums[i] % div == 0:
            nums.pop(i)        # a lista é diretamente modificada
        else:
            i += 1
    return nums

print("Test ->", r1 == remove_multiplos_v2(test_list, test_div)) # True

# Chatgpt:
# Quando removes, o próximo elemento “desliza” para o mesmo índice.
# Só aumentas o índice se não removeres, garantindo que nenhum elemento é saltado.

# Este exercício serve para explicar que, sendo as listas mutáveis,
# temos de ter atenção ao alterar listas dentro de um algoritmo,
# sendo normalmente mais fácil criar uma nova lista para o resultado