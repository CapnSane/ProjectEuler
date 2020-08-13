'''
Problem 5

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?

'''

import time

## If I need someday of this function

# def prime_check():
#     lista2 = []
#     for num in seq:  
#         if num > 1:  
#             for i in range(2,num):  
#                 if (num % i) == 0:  
#                     break  
#             else:  
#                 lista2.append(num)
#     return lista2

def range_f(start,end):
    return range(start,end+1)

def prime_factors(n):
    lista3 = []
    while n % 2 == 0:
        lista3.append(2)
        n = n / 2
    for i in range(3,int(n**0.5)+1,2):
        while n % i == 0:
            lista3.append(int(i))
            n = n / i
    if n > 2:
        lista3.append(int(n))
    return lista3

def p_factor_gen(seq):
    lista4 = []
    for i in seq:
        p = prime_factors(i)
        lista4.append(p)
    return lista4

def filtrar(dec):
    fil = {}
    for d in dec:
        n = d[0]
        if n not in fil:
            fil[n] = d
        else:
            if len(fil[n]) < len(d):
                fil[n] = d
    return fil

def product(fil):
    prod = 1
    lista = fil.values()
    for i in lista:
        for j in i:
            prod = prod * j
    return prod

def main():
    t0 = time.time()
    # 1. declarar a sequencia
    # seq = [2, 3, 4, 6, 8, 9, 16, 32]  # any sequence
    seq = range_f(2,20)

    # 2. decompor
    dec = p_factor_gen(seq)

    # 3. filtrar
    fil = filtrar(dec)

    # 4. Calcular a multiplicacao
    print(product(fil))
    t1 = time.time()
    print("Time elapsed: ", t1 - t0, "sec")

main()