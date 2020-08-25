'''
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

import time

def prime_sum(n):
    result = 0
    for num in range(2,n+1):
        if num > 1:     
            for i in range(2,(num//3)+2):  
                if (num % i) == 0:  
                    break  
            else:  
                result += num
    return result

def main():
    t0 = time.time()
    # Defining the limit
    limit = 2000000

    # Sum of all primes in the list
    result = prime_sum(limit)

    # Printing the answer
    print(result)
    t1 = time.time()
    print("Time elapsed: ", t1 - t0, "sec")

main()

# The answer: 142913828922
# Time elapsed of first version:  15934.882136821747 sec