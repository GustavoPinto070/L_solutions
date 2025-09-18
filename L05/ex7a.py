def valor(q: int, j: float, n: int) -> float:
    if n < 0 or j <= 0 or j >= 1 or q < 0:
        raise ValueError("Incorrect arguments")
    return q * (1 + j) ** n

# Test the function
if __name__ == "__main__":
    print("Enter the principal amount, interest rate, and number of periods to calculate the future value\n(-1 to exit)")
    while True:
        principal = int(input("Principal amount? "))
        if principal == -1:
            break
        interest_rate = float(input("Interest rate (as a decimal)? "))
        if interest_rate == -1:
            break
        periods = int(input("Number of periods? "))
        if periods == -1:
            break
        try:
            print(valor(principal, interest_rate, periods))
        except ValueError as e:
            print(e)