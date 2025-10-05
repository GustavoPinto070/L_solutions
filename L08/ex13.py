def aproxima_area(a, b, n):
    l = (b - a) / n
    area = 0
    for i in range(1, n + 1):
        x0 = a + (i - 1) * l
        x1 = a + i * l
        h = (f(x0) + f(x1)) / 2
        area += l * h
    return area

def f(x):
    return -(x - 2)**2 + 5

if __name__ == "__main__":
    print(aproxima_area(0.5, 3.5, 6))
    print(aproxima_area(0.5, 3.5, 12))
    print(aproxima_area(0.5, 3.5, 100))
