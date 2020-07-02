seq = [0,1]

def fibo(lim):
    i = 1
    while seq[i] < lim:
        if seq[i-1] > lim - seq[i]:
            break
        else:
            seq.append(seq[i-1] + seq[i])
            i += 1
    seq.remove(seq[0])
    seq.remove(seq[1])
    return sum(i for i in seq if i % 2 == 0)

print("A sequência de Fibonacci até o número limite é:")
print(seq, "\nA soma dos termos pares é:\n", fibo(4000000))