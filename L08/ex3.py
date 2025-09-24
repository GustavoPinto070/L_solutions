# this looks cool and flashy but actually sucks cause its calculating sums for each term (O(n^2) runtime)
def soma_cumulativa_noob(nums:list[int])->list[int]:
    return list(sum(nums[:i+1])for i in range(len(nums)))

def soma_cumulativa_pro(nums:list[int])->list[int]: # normal, best version with what we know (directly changes the list tho)
    soma = 0
    for i in range(len(nums)):
        soma += nums[i]
        nums[i] = soma
    return nums

def soma_cumulativa_god(l): # same as pro but less readable (directly changes the list tho still)
    s=0;return[(s:=s+x)for x in l]

def soma_cumulativa_cheater(nums:list[int])->list[int]: # cheats (the best, most realistic way to do it everyday)
    from itertools import accumulate
    return list(accumulate(nums))

test_list = [1, 2, 3, 4, 5]
print(r1:=(soma_cumulativa_noob(test_list.copy())))     # [1, 3, 6, 10, 15]
print(r2:=(soma_cumulativa_pro(test_list.copy())))      # [1, 3, 6, 10, 15]
print(r3:=(soma_cumulativa_god(test_list.copy())))      # [1, 3, 6, 10, 15]
print(r4:=(soma_cumulativa_cheater(test_list.copy())))  # [1, 3, 6, 10, 15]
print("Test ->", r1 == r2 == r3 == r4)                  # True