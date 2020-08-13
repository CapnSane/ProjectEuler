"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

import math
import numpy as np

def multiples_sum(lim,*numeros):
    div = np.lcm.reduce(numeros)
    return sum([i for i in range(0,lim,div)])

def main():
    # Defining the range limit (given by the problem statement)
    value = 1000

    # Defining the multiples of 3 and 5
    mult_3 = multiples_sum(value,3)
    mult_5 = multiples_sum(value,5)

    # Defining the repeated multiples of 3 and 5 at the same time
    mult_3_5 = multiples_sum(value,3,5)

    # Calculating the sum of all the multiples of 3 or 5 below 1000
    answer = mult_3 + mult_5 - mult_3_5

    # Printing the result
    print(answer)

main()