''' 
' Euler58.py
' (c) Riwaz Poudyal
' ~7secs, Sept 2017. isPrime() is the bottleneck and can be replacd with a seiv' e.
'''

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

diag = [3, 5, 7, 9]
primes = 3
length = 3
total = 5

while (primes * 1.0 / total > 0.1):
    diag[0] = diag[3] + length + 1
    for i in range(1, 4):
        diag[i] = diag[i-1] + length + 1
    for num in diag:
        if isPrime(num):
            primes += 1
    total += 4
    length += 2
print(length)
