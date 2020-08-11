import math
'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

lista = []
value = 600851475143

def prime_factors(n):
    while n % 2 == 0:
        lista.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            lista.append(int(i))
            n = n / i
    if n > 2:
        lista.append(int(n))

prime_factors(value)
largest_prime = lista[-1]
print(lista)
print(largest_prime)

