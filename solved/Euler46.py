# Euler46.py
# (c) 2016 RIWAZ POUDYAL 
# 0.05 secs 4 nov 2016


primes = []
squares = []

l = [False] * 50000
l[1] = True
l[0] = True


def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    i = 5
    while(i*i <= n):
        if n % i == 0: return False
        if n % (i + 2) == 0: return False
        i += 6
    return True

for i in range(0, 5000):
    if isPrime(i):
        primes.append(i)

for i in range(0, 100):
    squares.append(2 * i * i)


for x in primes:
    for y in squares:
        l[x + y] = True

for i in range(1, len(l), 2):
    if not l[i] and not isPrime(i):
        print(i)
        break
