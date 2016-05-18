''' Euler37.py
'   (c) Riwaz Poudyal 2016
'   0.85 secs
'''

l = [-1] * 1000000
l[1] = 0
def isPrime(n):
    if l[n] == 1: return True
    elif l[n] == 0: return False
    else:
        i = 2
        while(n >= i*i):
            if n % i == 0: 
                l[n] = 0
                return False
            i += 1
        l[n] = 1
        return True

def isTurnRight(n):
    while (n > 0):
        if (not isPrime(n)):
            return False
        n = int (n/10)
    return True

def isTurnLeft(n):
    div = 10
    i = n % 10
    while(i != n):
        if (not isPrime(i)): return False
        div *= 10
        i = n % div
    return True

a = 10
found = 0
tList = []
while(found < 11):
    if isTurnLeft(a) and isTurnRight(a):
        print(a)
        tList.append(a)
        found += 1
    a += 1

sum = 0
for x in tList:
    sum += x

print(sum)
