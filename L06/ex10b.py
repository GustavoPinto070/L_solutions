def descodifica(str:str)->str:
    resultado = ""
    if len(str) % 2 == 1:
        for i in range(len(str)//2):
            resultado += str[i]
            resultado += str[i + len(str)//2+1]
        resultado += str[len(str)//2]
    else:
        for i in range(len(str)//2):
            resultado += str[i]
            resultado += str[i + len(str)//2]
    return resultado

# Test the function
if __name__ == "__main__":
    print("Introduza uma sequência de characters\n(-1 to exit)")
    while True:
        str = input("? ")
        if str == "-1":
            break
        print(descodifica(str))
    
