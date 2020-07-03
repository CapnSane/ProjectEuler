lista = {}

def function(a):
    return a == a[::-1]
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if function(str(i*j)):
            lista[i*j] = (i,j)
            break

max_key = max(lista)

print("The largest palindrome made from the product of two 3-digit numbers is:", max_key)
print("The two 3-digit numbers that make it are:", lista[max_key])
