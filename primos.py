import math
def checar(p):
        while True:
                try:
                    numero = int(input(f"Por favor, insira um número maior que 1: "))
                    if numero > 1:
                        return numero
                    else:
                        print("Erro: o número deve ser maior que 1. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. insira outro número.")
p = 1
n = checar(p)
numerosp = []

for x in range (2, n + 1):
    div = 0
    for i in range(1, n + 1):
        if x % i == 0:
            div += 1
    if div == 2:
        numerosp += [x]
             
print (f'Estes são todos os numeros primos entre 0 e {n}: {numerosp} ')
