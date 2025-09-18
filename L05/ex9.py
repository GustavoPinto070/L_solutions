def dia_da_semana(dia: int, mes: int, ano: int) -> str:
    def dia_traduzido(h: int) -> str:
        if h == 0:
            return "Sábado"
        elif h == 1:
            return "Domingo"
        elif h == 2:
            return "Segunda-feira"
        elif h == 3:
            return "Terça-feira"
        elif h == 4:
            return "Quarta-feira"
        elif h == 5:
            return "Quinta-feira"
        elif h == 6:
            return "Sexta-feira"
        else:
            raise ValueError("Something went wrong ;-;")
    if mes < 3:
        mes += 12
        ano -= 1
    k = ano % 100
    j = ano // 100
    h = (dia + (13 * (mes + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)) % 7
    return dia_traduzido(h)

# Test the function
if __name__ == "__main__":
    print("Enter a date to find out the day of the week\n(-1 to exit)")
    while True:
        day = int(input("Day? "))
        if day == -1:
            break
        month = int(input("Month? "))
        if month == -1:
            break
        year = int(input("Year? "))
        if year == -1:
            break
        print(dia_da_semana(day, month, year))
