''' Euler49.py
'   (c) Riwaz Poudyal 2016
'   0.085 secs (016 May 18)
'''

from itertools import permutations

l = [-1] * 10000
done = [False] * 10000 #Permutations we have already checked and need not recheck

def isPrime(n):
    if l[n] == 0:
        return False
    elif l[n] == 1:
        return True
    else:
        i = 2
        while(i*i <= n):
            if n % i == 0:
                l[n] = 0
                return False
            i += 1
        l[n] = 1
        return True

# Return list of all 4 digit permutations
def returnPermute(i):
    lst = [int(x) for x in str(i)]
    lst = list(permutations(lst))
    perm = []
    for (a,b,c,d) in lst:
        perm.append(a*1000 + b*100 + c*10 + d)
    return perm

# All numbers with more than 2 permutations that are prime
seq = []

for i in range(1000,9999):
    if not done[i]:
        z = []
        for x in returnPermute(i):
            if x > 1000:
                done[x] = True
                if isPrime(x) and x not in z:
                    z.append(x)
        if len(z) > 2:
            seq.append(z)

# Check the 3330 difference property
final = []
for z in seq:
    z.sort()
    for x in z:
        if (x + 3330 in z) and (x + 3330 + 3330 in z):
            final.append(x)

# Only two numbers!
for a in final:
    print (str(a) + str(a+3330) + str(a+3330+3330))
