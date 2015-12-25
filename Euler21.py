''' Eular21.py
'   (c) 2015 Riwaz Poudyal
'   0.28 secs
'''

def amicable(n):
    i = 2
    sum = 1
    while ( i * i <= n):
        if n % i == 0: 
            sum += i
            sum += (n/i)
        i += 1
    return int(sum)

s = 0 
for x in range(2,10000):
    am = amicable(x)
    if am != x and amicable(am) == x: s += x

print(s)
