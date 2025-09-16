s = int(input("Escreva o número de segundos "))
print(f"dias: {s//86400}; horas: {(s%86400)//3600}; minutos: {(s%3600)//60}; segundos: {s%60}")