def media_digitos(num: int) -> float:
    soma = 0
    i = 0
    while num > 0:
        soma += num % 10
        num //= 10
        i += 1
    if i == 0:
        return 0.0
    return soma / i

# Test the function
if __name__ == "__main__":
    print("Enter an integer to calculate the average of its digits\n(-1 to exit)")
    while True:
        number = int(input("Number? "))
        if number == -1:
            break
        print(media_digitos(number))