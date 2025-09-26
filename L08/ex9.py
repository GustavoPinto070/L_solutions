def num_occ_lista(lista:list[int|list], num:int)->int:
    count = 0
    for x in lista:
        if isinstance(x, list):
            count += num_occ_lista(x, num) # recursivamente
        elif x == num:
            count += 1
    return count

# same thing but unreadable
def num_occ_lista_pro(l,n): return sum(num_occ_lista_pro(x,n) if isinstance(x,list)else 1 if x==n else 0 for x in l)

if __name__ == "__main__":
    test_list = [1, [[[1]], 2], [[[2]]], 2]
    print(r1:=(num_occ_lista(test_list, 2)))
    print(r2:=(num_occ_lista_pro(test_list, 2)))
    print("Test ->", r1 == r2)