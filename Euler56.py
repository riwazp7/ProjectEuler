''' Euler56.py
'   (c) 2015 Riwaz Poudyal
'   0.33 secs
'''
sum = 0

for a in range(1,101):
    for b in range(1,101):
        
        n = str(a**b)
        s = 0
        for x in n:
            s += int(x)
        
        if (s > sum): sum = s



print (sum)
