def reconhece(p, s) -> bool:
    i = j = 0
    while i < len(p):

        if j == len(s):
            j += 1
            if j == len(s):
                return True
        
        else:
            i -= j # i volta ao inicial + 1 (repete a sequência partindo do i inicial + 1 elemento)
            j = 0
        
        i += 1
    
    return False

if __name__ == "__main__":
    print(reconhece([7, 4, 7, 4, 3, 7, 2, 7], [7, 4, 3]))