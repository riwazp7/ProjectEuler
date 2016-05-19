''' Euler32.py
'   (c) Riwaz Poudyal 2016
'   0.21 secs (016 May 18)
'''

l_pan = []
sum = 0

def isPandigital(n):
    if n > 987654321 or n < 123456789: return False
    l = [1,2,3,4,5,6,7,8,9]
    while (n != 0):
        i = n % 10
        if not i in l:
            return False
        else:
            l.remove(i)
        n //= 10
    return True

for i in range(1,1980):
    for j in range(1,50):
        s = str(i) + str(j) + str(i*j)
        if isPandigital(int(s)):
            if not i * j in l_pan:
                l_pan.append(i*j)
                sum += (i*j)

print(sum)
