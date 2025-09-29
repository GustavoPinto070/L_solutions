def euromilhoes() -> list[list[int]]:
    
    def inteiro_aleatorio(start: int, stop: int) -> int:
        from random import random
        """
        random = [0, 1[
        0 <= r < 1
        0 <= r < distancia + 1 (se distancia = 49, 50)
        0.5 <= r < distancia + 1.5 (se start = 1)
        int(0.5 <= r < 49 + 1.5) <=> 1 <= r <= 50
        com todos os elementos com probabilidade igual
        """
        return int(random()*(stop - start + 1) + start - 0.5)
    
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
    print("\n".join(str(euromilhoes()) for _ in range(99)))