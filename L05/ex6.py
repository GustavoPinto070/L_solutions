from ex5 import bissexto

def dias_mes_but_better(mes, ano):
    dias_por_mes = {"jan": 31, "mar": 31, "abr": 30, "mai": 31, "jun": 30, "jul": 31, "ago": 31, "set": 30, "out": 31, "nov": 30, "dez": 31}
    if mes == "fev":
        if bissexto(ano):
            return 29
        return 28
    elif mes in dias_por_mes:
        return dias_por_mes[mes]
    else:
        raise ValueError("Mes nao existe")

# I refuse to do 13 if statements so chatgpt will do it *whips*
def dias_mes(mes, ano):
    if mes == "jan":
        return 31
    elif mes == "fev":
        if bissexto(ano):
            return 29
        else:
            return 28
    elif mes == "mar":
        return 31
    elif mes == "abr":
        return 30
    elif mes == "mai":
        return 31
    elif mes == "jun":
        return 30
    elif mes == "jul":
        return 31
    elif mes == "ago":
        return 31
    elif mes == "set":
        return 30
    elif mes == "out":
        return 31
    elif mes == "nov":
        return 30
    elif mes == "dez":
        return 31
    else:
        raise ValueError("Mes nao existe")

# Test the function
if __name__ == "__main__":
    print("Enter a month (3-letter abbreviation) and a year to determine the number of days in that month\n(-1 to exit)")
    while True:
        month = input("Month? ")
        if month == "-1":
            break
        year = int(input("Year? "))
        if year == -1:
            break
        try:
            print(dias_mes(month, year))
        except ValueError as e:
            print(e)