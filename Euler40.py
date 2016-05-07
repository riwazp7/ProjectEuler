''' Euler40.py
'   (c) Riwaz Poudyal 2016
'   0.15 secs
'''

s = ""
i = 1
while(len(s) < 1000000):
    s += str(i)
    i += 1

n = int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])
print(n)
    
