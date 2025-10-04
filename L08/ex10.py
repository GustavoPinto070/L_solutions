def euromilhoes() -> list[list[int]]:
    def inteiro_aleatorio(start: int, stop: int) -> int:
        from random import random
        """
        random = [0, 1[
        0 <= r < 1
        0 <= r < distancia + 1 (se distancia = 49, 50)
        int(1 <= r < 51) <=> 1 <= r <= 50 (r ∈ N)
        """
        return int(random()*(stop - start + 2) + start)
    
    def lista_inteiros_unicos_aleatorios(num_elementos: int, start: int, stop: int) -> list[int]:
        nums = []
        while len(nums) < num_elementos:
            num = inteiro_aleatorio(start, stop)
            if not num in nums:
                nums.append(num)
        return nums
    
    numeros = lista_inteiros_unicos_aleatorios(5, 1, 50)
    estrelas = lista_inteiros_unicos_aleatorios(2, 1, 12)
    return [numeros, estrelas]

if __name__ == "__main__":
    amount = int(input("How many? (int) "))
    print("\n".join(str(euromilhoes()) for _ in range(amount)))