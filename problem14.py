'''
Problem 14

Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

OBS.: Once the chain starts the terms are allowed to go above one million.

'''

def collatz(start):
  i = 1
  if start == 0:
    return 1
  else:
    while start != 1:
      if start % 2 == 0:
        start = int(start / 2)
        i += 1
      else:
        start = int(start * 3 +1)
        i += 1
  return i

def compare(num):
  x = 0
  i = 1
  save = 0
  for i in range(1, num, 1):
    if collatz(i) > save:
      save = collatz(i)
      x = i
    else:
      pass
  return x

print(compare(1000000))