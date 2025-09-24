def codifica(str:str)->str:
    return str[::2] + str[1::2]

# Test the function
if __name__ == "__main__":
    print("Introduza uma sequência de characters\n(-1 to exit)")
    while True:
        str = input("? ")
        if str == "-1":
            break
        print(codifica(str))