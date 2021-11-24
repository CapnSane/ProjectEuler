'''
Problem 15

Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

'''

import math

x = 20

def lattice(x):
  y = math.factorial(2*x)/math.factorial(x)**2
  return int(y)

print(lattice(x))