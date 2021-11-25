'''
Problem 16

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

'''

exp = 1000
x = 2**exp
sum = 0
for i in str(x):
  sum += int(i)

print(sum)
