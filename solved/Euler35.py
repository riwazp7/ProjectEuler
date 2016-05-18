''' Euler35.py
'   (c) 2015 Riwaz Poudyal. Thanks to www.prekshakoirala.com for debugging help
'   10.75 secs: can speed up with a lookup table to find if a number is prime.
'''


n = 0
def isPrime(i):
    if i <= 1:
        return False
 
    k = 2
    while (k*k <=i):
        if i % k == 0:
            return False
        k += 1
    return True
 
 
 
 
for z in range(0, 1000000):
    list = []
 
    if isPrime(z):
        i = z
        flag = True
        a = str(i)
 
        for x in xrange(len(str(i))):
 
            a = (a[1:]+ a[0])
            i = int(a)
 
            if not isPrime(i):
                flag = False
                break
 
        if flag: n += 1
 
 
print (n)
