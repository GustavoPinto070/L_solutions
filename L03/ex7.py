h = float(input("O número de horas trabalhadas (por semana): "))
sh = float(input("O salário por hora (em euros, €): "))
bonus = 2
if h <= 40:
    s = h * sh
else:
    s = 40 * sh + (h - 40) * sh * bonus
print(f"O salário semanal é {s:.2f} €")