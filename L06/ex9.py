def reconhece(str:str)->bool:
    i = 0
    while i < len(str) and str[i] in "ABCD":
        i += 1
    letras = i
    if letras == 0:     # No letters exist
        return False
    while i < len(str) and str[i] in "1234":
        i += 1
    numeros = i - letras
    if numeros == 0:     # No numbers exist
        return False 
    return i == len(str) # There is nothing else after the last numbers

# Test the function
if __name__ == "__main__":
    print("Introduza uma sequência de letras (ABCD) e números(1234)\n(-1 to exit)")
    while True:
        str = input("? ")
        if str == "-1":
            break
        print("Reconhece?", reconhece(str))