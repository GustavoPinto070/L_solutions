def apaga1(tuplo:tuple, num:int)->tuple:
    for i, n in enumerate(tuplo): 
        if n == num:
            return tuplo[:i] + tuplo[i+1:]
    return tuplo

# Test the function
if __name__ == "__main__":
    print("Introduza um tuplo de inteiros e um inteiro\n(-1 to exit)")
    while True:
        t = eval(input("tuplo? "))
        if t == -1:
            break
        n = int(input("n? "))
        print(apaga1(t,n))