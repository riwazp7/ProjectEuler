#Returns if n is abundant
def ali(n):
    sum = -n
    i = 1
    while ( i * i < n):
        if n % i == 0: 
            sum += i
            if ( (n / i) != i): sum += (n/i)
        i += 1
    return (sum > n)

#Find all abundant numbers below 28123
l = []
for x in range(12,28123):
    if ali(x): l.append(x)

# Index = Number; value True if it can be written as a sum
abundants = [False] * 28123

for a in l:
    for z in l:
        if (a+z) < len(abundants):
            abundants[a+z] = True

print(abundants)
s = 0
for i in range(1,len(abundants)):
    if not abundants[i]: s += i

print (s)

