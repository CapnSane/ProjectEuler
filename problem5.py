import math
import time

t0 = time.time()
lista = []

def div_list(x,start,end):
    for n in range(start,end+1):
        if x % n == 0:
            lista.append(n)
        else:
            pass

def minor_Number(start,end):
    y = 1
    while True:
        div_list(y,start,end)
        # print(y,lista)
        y += 1
        if lista == [i for i in range(start,end+1)]:
            print("The answer is", y-1)
            break
        lista.clear()
print(minor_Number(2,20))

t1 = time.time() - t0
print("Time elapsed: ", t1)

# The answer is 232792560
# Time elapsed:  2944.0374722480774
