''' Euler48.py
'   (c) Riwaz Poudyal
'   0.045 secs
'''


sum = 0
for x in range(1,1001):
    sum += x**x
s = str(sum)
print (s[len(s)-10:])
