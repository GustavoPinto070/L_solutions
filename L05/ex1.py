def cinco(x)-> str:
    return x==5

# Test the function
if __name__ == "__main__":
    print("Enter a number or calculation to determine if it is equal to 5\n(-1 to exit)")
    while True:
        x = eval(input("? "))
        if x == -1:
            break
        print(cinco(x))