'''
Problem 6

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is

3025 - 285 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
'''

def rangeF(start,end):
    return range(start, end + 1)

def sum_Squares(seq):
    sum_S = 0
    for i in seq:
        sum_S = sum_S + i**2
    return sum_S

def square_Sum(seq):
    sum_range = 0
    for i in seq:
        sum_range = sum_range + i
    square = sum_range**2
    return square

def subtrac(x1,x2):
    total = x1 - x2
    return total

def main():
    # Range definition:
    seq = rangeF(1,100)

    # The sum of the squares calculation:
    sumS = sum_Squares(seq)

    # The square of the sum calculation:
    squareS = square_Sum(seq)

    # The difference between the sum of the squares and the square of the sum:
    sub = subtrac(squareS,sumS)

    # The result:
    print(sub)

main()
