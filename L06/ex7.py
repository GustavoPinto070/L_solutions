def amigas(amiga1: str, amiga2: str)->bool:
    count = 0
    for i in range(min(len(amiga1), len(amiga2))):
        if amiga1[i] == amiga2[i]:
            count += 1
    total = max(len(amiga1), len(amiga2))
    if total == 0 or 1 - (count/total) > 0.1:
        return False
    return True

# Test the function
if __name__ == "__main__":
    print("Introduza duas palavras não vazias\n(-1 to exit)")
    while True:
        p1 = input("1? ")
        if p1 == "-1":
            break
        p2 = input("2? ")
        if p2 == "-2":
            break
        print("São amigas?", amigas(p1, p2))