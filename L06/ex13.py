from ex12 import apaga1

def permutacao(t1:tuple, t2:tuple)->bool:
    for num in t1:
        if t2 == None:            # t2 menor que t1
            return False
        t1 = apaga1(t1, num)
        if t2 == apaga1(t2, num): # num de t1 não está em t2
            return False
        t2 = apaga1(t2, num)
    return t1 == t2               # falso se t1 menor que t2

if __name__ == "__main__":
    print(permutacao((1, 2, 3), (1, 2, 3)))
    print(permutacao((1, 2, 3), (2, 3, 1)))
    print(permutacao((1, 1, 1, 2, 3), (1, 2, 3)))
    print(permutacao((1, 2, 3), (1, 2, 3, 4)))