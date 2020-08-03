import math
import numpy as np

"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

value = 1000

def multiples_sum(lim,*numeros):
    div = np.lcm.reduce(numeros)
    return sum([i for i in range(0,lim,div)])

print(multiples_sum(value,3) + multiples_sum(value,5) - multiples_sum(value,3,5))