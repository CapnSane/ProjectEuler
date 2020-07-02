import math
# def primo(number):
#     for i in range(2, number):
#         if (number % i) == 0:
#             # print(number, "is not a prime.")
#             False
#             break
#     else:
#         # print(number, "is a prime.")
#         True

lista = []
value = 600851475143

def primeFactors(n):
    while n % 2 == 0:
        lista.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            lista.append(int(i))
            n = n / i
    if n > 2:
        lista.append(int(n))

primeFactors(value)
largest_prime = lista[-1]
print(lista)
print(largest_prime)

