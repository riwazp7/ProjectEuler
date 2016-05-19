''' Euler47.py
'   (c) 2016 Riwaz Poudyal
'   6 secs. Easy improvements possible (just divide by primes in a list)
'''

p = [-1] * 200000

def findPrime(n):
    global p
    if p[n] != -1: return p[n]
    c = n
    l = []
    i = 2
    while (i * i <= n):
        while c % i == 0:
            c /= i
            if i not in l:
                l.append(i)
        i += 1
    if c != 1 and c not in l:
        l.append(int(c))
    p[n] = len(l)
    return p[n]

i = 50000
while(True):
    if findPrime(i) > 3 and findPrime(i+1) > 3 and findPrime(i+2) > 3 and findPrime(i+3) > 3:
        print(i)
        break
    i += 1
