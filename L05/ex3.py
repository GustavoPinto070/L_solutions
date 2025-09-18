def area_circulo(radio: float) -> float:
    pi = 3.14
    return pi * radio ** 2

# Test the function
if __name__ == "__main__":
    print("Enter a radius to calculate the area of a circle\n(-1 to exit)")
    while True:
        radio = float(input("? "))
        if radio == -1:
            break
        print(area_circulo(radio))