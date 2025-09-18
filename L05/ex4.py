from ex3 import area_circulo
def area_coroa(r1: float, r2: float) -> float:
    if r1 >= r2:
        raise ValueError("The outer radius must be greater than the inner radius")
    return area_circulo(r2) - area_circulo(r1)

# Test the function
if __name__ == "__main__":
    print("Enter the inner and outer radius to calculate the area of a circular crown\n(-1 to exit)")
    while True:
        inner_radius = float(input("Inner radius? "))
        if inner_radius == -1:
            break
        outer_radius = float(input("Outer radius? "))
        if outer_radius == -1:
            break
        try:
            print(area_coroa(inner_radius, outer_radius))
        except ValueError as e:
            print(e)