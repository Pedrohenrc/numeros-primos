
import math
n = int(input("insira o numero:"))
if n in (0, 1, 2):
        print(f'não há nenhum número primo entre 0 e {n}')
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