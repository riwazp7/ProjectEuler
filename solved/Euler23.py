import math

#Returns if n is abundant
def ali(n):
    sum = -n
    for i in range(1,int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            sum += i
            if ((n / i) != i): sum += (n/i)

    return (sum > n)

#Find all abundant numbers below 28123
l = []
for x in range(12,28123):
    if ali(x): l.append(x)

print("List of abundant #s built")

# Index = Number; value True if it can be written as a sum
abundants = [False] * 28123

for i in range(0,len(l)):
    for z in range(i, len(l)):
        if (l[i] + l[z]) < len(abundants): abundants[l[i] + l[z]] = True

print("Adding numbers that cannnot be written as sum")

s = 0
for i in range(1,len(abundants)):
    if not abundants[i]: s += i

print (s)