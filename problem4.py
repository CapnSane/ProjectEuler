'''
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def palindrome(a):
    return a == a[::-1]

def product(n):
    palindromes  = {}
    for i in range(10**(n-1), 10**n):
        for j in range(i, 10**n):
            if palindrome(str(i*j)):
                palindromes[i*j] = (i,j)
    return palindromes

def main():
    # Defining the function that gives a palindrome number

    # Defining n of n-digit
    n = 3

    # Defining a function that generates a list of palindromes made from the product of two 3-digit numbers
    palindromes = product(n)

    # Taking the min and max number from the list
    min_key = min(palindromes)
    max_key = max(palindromes)

    # Printing the answer
    print("The lowest palindrome made from the product of two 3-digit numbers is:", min_key)
    print("The two 3-digit numbers that make the lowest palindrome are:", palindromes[min_key])
    print("------------------------------------------------------------------------------")
    print("The largest palindrome made from the product of two 3-digit numbers is:", max_key)
    print("The two 3-digit numbers that make the largest palindrome are:", palindromes[max_key])
    print("\n The answer is", max_key)

main()