''' Euler26.py
'   (c) Riwaz Poudyal 2016
'   0.23 secs Sept 13 016 
'''
from decimal import *
getcontext().prec = 2000

longest = 1
d = -1

#Just a few zeros so slight inefficiency okay
def removeLeadingZeros(s):
    while(s.startswith('0')):
        s = s[1:]
    return s

def getDecimalString(x):
    n = Decimal(1) / Decimal(x)
    return removeLeadingZeros(str(n)[2:]) # Now we have the String

def getLongestCycle(s):
    for i in range(0, len(s) - 1): # for each position in the string
        for j in range(1, int(len(s) / 2) + 1): # Consider substring of every possible length
            if s[i:i+j] == s[i+j:i+2 * j]:
                return j
    return 1


for i in range(3,1000):
    decimalString = getDecimalString(i)
    cycle_length = getLongestCycle(decimalString)
    if (cycle_length > longest):
        longest = cycle_length
        d = i

print (d)

