import math
import numpy as np

value = 1000

def multiples_sum(lim,*numeros):
    div = np.lcm.reduce(numeros)
    return sum([i for i in range(0,lim,div)])

print(multiples_sum(value,3) + multiples_sum(value,5) - multiples_sum(value,3,5))