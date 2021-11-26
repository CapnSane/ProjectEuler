'''
Problem 17

If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

Obs.: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

'''

from num2words import num2words

x = 42

n = 1
max = 1000
newword = ""

for i in range(n, max + 1, 1):
  word = num2words(i)
  newword += word

total = (newword.replace("-","")).replace(" ","")

print(len(total))
