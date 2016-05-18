# Euler20.py
# (c) 2015 Riwaz Poudyal
# There are 0s in the end but adding them isn't a problem


n = 36288
for i in range(11,100):
    n*=i

s = str(n)
sum = 0
for x in s:
    sum += ( int(x))

print (sum)
