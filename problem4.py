lista = {}

def function(a):
    return a == a[::-1]
for i in range(999,101,-1):
    for j in range(999,i-1,-1):
        if function(str(i*j)):
            lista[i*j] = (i,j)
            # break

min_key = min(lista)
max_key = max(lista)

print("The lowest palindrome made from the product of two 3-digit numbers is:", min_key)
print("The two 3-digit numbers that make the lowest palindrome are:", lista[min_key])
print("------------------------------------------------------------------------------")
print("The largest palindrome made from the product of two 3-digit numbers is:", max_key)
print("The two 3-digit numbers that make the largest palindrome are:", lista[max_key])