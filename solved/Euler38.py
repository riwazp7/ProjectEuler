''' Euler38.py
'   (c) Riwaz Poudyal 2016
'   0.06 s (May 6 016)
'''

def isPandigital(n):
    l = ["1","2","3","4","5","6","7","8","9"]
    for x in str(n):
        if x in l:
            l.remove(x)
        else: return False
    if len(l) == 0: return True
    return False

largest = 0
a = 1

while(a<10000):
    s = ""
    n = 1
    while(len(s) < 9):
        s += (str(a * n))
        n += 1
    if len(s) == 9 and isPandigital(int(s)) and largest < int(s):
        largest = int(s)
        print(largest)
    a += 1
