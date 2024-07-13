import math
def checar(p):
        while True:
                try:
                    numero = int(input("Por favor, insira um número maior que 1: "))
                    if numero > 1:
                        return numero
                    else:
                        print("Erro: o número deve ser maior que 1. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. insira outro número.")
p = 1
n = checar(p)
def primo(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def numerosp(n):
    listap = []
    for x in range (1,(n + 1):
        if primo(x):
            listap += [x]
    return listap
        
print (f"Números primos até {n}: {numerosp(n)}")
