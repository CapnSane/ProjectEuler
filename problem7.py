'''
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

import time

def prime_gen(n):
    lista = []
    num = 1
    while len(lista) != n:
        if num > 1:     
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:  
                lista.append(num)
        num += 1
    return lista[n-1]

def main():
    t0 = time.time()
    # Defining the prime number that will be shown:
    n = 10001

    # nth prime generator (in the case of problem, the 10001st):
    nth = prime_gen(n)

    # Printing the number:
    print(nth)
    t1 = time.time()
    print("Time elapsed: ", t1 - t0, "sec")

main()