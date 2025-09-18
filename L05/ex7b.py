from ex7a import valor # I also don't get why this is needed
from math import log

def duplicar(q: int, j: float) -> int: # q não interessa para o cálculo
    return int(log(2) / log(1 + j)) # Se sqrt é permitido, log também deve ser

"""
2q = q * (1 + j)**n
2 = (1 + j)**n
log(2) = log((1 + j)**n)
log(2) = n * log(1 + j)
n = log(2) / log(1 + j)
"""

# Test the function
if __name__ == "__main__":
    print("Enter the principal amount and interest rate to calculate the number of periods to double the investment\n(-1 to exit)")
    while True:
        principal = int(input("Principal amount? ")) # Doesn't matter for the calculation but is asked in the example
        if principal == -1:
            break
        interest_rate = float(input("Interest rate (as a decimal)? "))
        if interest_rate == -1:
            break
        try:
            print(duplicar(principal, interest_rate))
        except ValueError as e:
            print(e)