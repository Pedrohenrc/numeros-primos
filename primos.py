import math
import sys
n = int(input("insira o numero maior que 1:"))
if n in (0, 1):
        print('Entrada inválida.')
        sys.exit()
if n == 2:
    print(f'Não há nenhum número primo entre 0 e {n}')
    sys.exit()
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
    for x in range (1, n):
        if primo(x):
            listap += [x]
    return listap
        
print (f"Números primos até {n}: {numerosp(n)}")
