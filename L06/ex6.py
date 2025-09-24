def num_para_seq_cod(n:int)->tuple:
    resultado = ()
    while n > 0:
        ultimo_digito = n % 10      # retrieve last digit
        n //= 10                    # remove last digit
        if ultimo_digito % 2 == 0:  # se par
            ultimo_digito += 2      # próx. par
        else:                       # se ímpar
            ultimo_digito -= 2      # ímpar anterior
        ultimo_digito %= 10         # -1 into 9 and 10 into 0
        resultado += (ultimo_digito,)
    return resultado[::-1]

def num_para_seq_cod_pro(n:int)->tuple:
    resultado = ()
    while n > 0:
        ultimo_digito = n % 10
        n //= 10
        ultimo_digito=(ultimo_digito+2*(-1)**(ultimo_digito%2))%10 # lines 6 -> 10
        resultado += (ultimo_digito,)
    return resultado[::-1]

def num_para_seq_cod_god(n): # cool
    return tuple((int(l)+2*(-1)**(int(l)%2))%10 for l in str(n))

# Test the function
if __name__ == "__main__":
    print("Introduza um número inteiro positivo\n(-1 to exit)")
    while True:
        n = int(input("? "))
        if n == -1:
            break
        print(r1:=(num_para_seq_cod(n)))
        print("Test ->", r1 == num_para_seq_cod_god(n) == num_para_seq_cod_pro(n)) # True
        