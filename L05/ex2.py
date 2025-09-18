def horas_dias(horas: int) -> float:
    return horas/24

# Test the function
if __name__ == "__main__":
    print("Enter a number of hours to convert to days\n(-1 to exit)")
    while True:
        horas = int(input("? "))
        if horas == -1:
            break
        print(horas_dias(horas))