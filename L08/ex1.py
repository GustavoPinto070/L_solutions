def lista_codigos(str): # I love type annotations or type hints, hate not using them
    list = []
    for char in str:
        list.append(id(char))
    return list

# another way to write; a generator having id(char) for each char in the string, converted into a list
def lista_codigos_v2(str:str)->list[int]: 
    return list(ord(char) for char in str)

print(r1:=(lista_codigos('bom dia')))   # walrus (:=) assigns and uses a variable in a single line
print("Test ->", r1 == lista_codigos_v2('bom dia')) # Testing if both algorithms return the same thing

# prints:
# [98, 111, 109, 32, 100, 105, 97]
# Test -> True

# everything is extra besides the first 5 lines, dw