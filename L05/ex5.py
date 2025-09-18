def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

# Test the function
if __name__ == "__main__":
    print("Enter a year to determine if it is a leap year\n(-1 to exit)")
    while True:
        year = float(input("? "))
        if year == -1:
            break
        print(bissexto(year))
        