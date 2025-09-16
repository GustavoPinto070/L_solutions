km = float(input("Introduza a distância percorrida em Km: "))
min = float(input("Introduza o tempo necessário em minutos: "))
kmh = km/(min/60)
ms = (km*1000)/(min*60)
print(f"A sua velocidade média foi {kmh:.2f} Km/h ou {ms:.2f} m/s")
# Same as
print("A sua velocidade média foi", round(kmh, 2), "Km/h ou", round(ms, 2), "m/s")
# Without f-strings or the round() function
print("A sua velocidade média foi", int(kmh*100)/100, "Km/h ou", int(ms*100)/100, "m/s")
# Without rounding
print("A sua velocidade média foi", kmh, "Km/h ou", ms, "m/s")

# In an f-string, you can use :.2f to format a float to 2 decimal places
# Also you can do (x:.2f).rstrip('0').rstrip('.') to remove trailing zeros and the decimal point if not needed