def serie_geom(r: int|float, n: int) -> float:
    if type(n) is not int or n < 0:
        raise ValueError("serie_geom: argumento")
    i = 0
    s = 0.0
    while i <= n:
        s += r**i
        i += 1
    return s

# Test the function
if __name__ == "__main__":
    print("Enter the ratio and number of terms to calculate the geometric series sum\n(-1 to exit)")
    while True:
        ratio = float(input("Ratio? "))
        if ratio == -1:
            break
        terms = int(input("Number of terms? "))
        if terms == -1:
            break
        try:
            print(serie_geom(ratio, terms))
        except ValueError as e:
            print(e)