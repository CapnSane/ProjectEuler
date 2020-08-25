'''
Problem 9


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

import time

def list_gen(last):
    triplet = [[a, b, c] for a in range(1,last-1)
    for b in range(1,last)
        for c in range(1,last+1) if a != b and a != c and b != c and a < b and b < c] 
    return triplet

def conditions(lista,total):
    new = []
    for i in range(len(lista) + 1):
        if (lista[i][0] + lista[i][1] + lista[i][2]) == total and (lista[i][0]**2 + lista[i][1]**2) == lista[i][2]**2:
            return lista[i]

def main():
    t0 = time.time()
    # Definitions - Range and total of sum
    last = 500
    total = 1000

    # Generating the triplet list in a range
    lista = list_gen(last)

    # Applying the conditions and getting the triplet
    new_list = conditions(lista,total)

    # Multiplying a * b * c
    product = new_list[0] * new_list[1] * new_list[2]

    # Printing the answer
    print(product)
    t1 = time.time()
    print("Time elapsed: ", t1 - t0, "sec")

main()