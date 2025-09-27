def num_occ_lista(lista:list[int|list], num:int)->int:
    count = 0
    for x in lista:
        if isinstance(x, list):
            count += num_occ_lista(x, num) # recursivamente
        elif x == num:
            count += 1
    return count

if __name__ == "__main__":
    # same thing but unreadable
    def f(l,n): return sum(f(x,n)if isinstance(x,list)else 1 if x==n else 0 for x in l)
    
    test_list = [1, [[[1]], 2], [[[2]]], 2]
    print(r1:=(num_occ_lista(test_list, 2))) # 3
    print(r2:=(f(test_list, 2))) # 3
    print("Test ->", r1 == r2) # True