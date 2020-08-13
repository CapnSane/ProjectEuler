'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

import math

def prime_factors(n,lista):
    while n % 2 == 0:
        lista.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            lista.append(int(i))
            n = n / i
    if n > 2:
        lista.append(int(n))

def main():
    # Defining the value given by the problem
    value = 600851475143

    # Generating the list of prime factors
    lista = []
    prime_factors(value,lista)

    # Getting the largest prime factor of the given value from the list
    largest_prime = lista[-1]

    # Printing the list
    print(lista)

    # Printing the answer (largest prime factor of the given value)
    print(largest_prime)

main()